import tictactoe.ReplayMemory as R
import tictactoe.QNet as QNet
import numpy as np
import torch
class QAgent():
    def __init__(self, lr, epsilon, eps_dec, eps_min, statespace, actionspace,
                 chkpt_dir, memorysize, batchsize, rplcinterv, gamma):
        super(QAgent, self).__init__()
        self.lr = lr
        self.gamma = gamma
        self.epsilon = epsilon
        self.eps_dec = eps_dec
        self.eps_min = eps_min
        self.statespace = statespace
        self.actionspace = actionspace
        self.chkpt_dir = chkpt_dir
        self.memorysize = memorysize
        self.batch_size = batchsize
        self.learncounter = 0
        self.replace_targetcntr = rplcinterv

        self.memory = R.ReplayBuffer(memorysize=self.memorysize, statespace=statespace)

        self.evalnet = QNet.DQNet(lr=self.lr, statespace=self.statespace, actionspace=self.actionspace,
                                  chkpt_dir=self.chkpt_dir+str("evalnet"))

        self.nextnet = QNet.DQNet(lr=self.lr, statespace=self.statespace, actionspace=self.actionspace,
                                  chkpt_dir=self.chkpt_dir+str("nextnet"))

    def save_models(self):
        self.evalnet.save_checkpoint()
        self.nextnet.save_checkpoint()

    def load_models(self):
        self.evalnet.load_checkpoint()
        self.nextnet.load_checkpoint()

    def replace_target_network(self):
        if self.learncounter % self.replace_targetcntr == 0:
            self.nextnet.load_state_dict(self.evalnet.state_dict())

    def choose_action(self, obs, posmovs):
        if np.random.random() > self.epsilon:
            obs = torch.Tensor([obs])
            obs = obs.to(self.evalnet.device)
            actions = self.evalnet.forward(obs)
            action = torch.argmax(actions).item() + 1
            self.learncounter += 1
            return action
        else:
            action = np.random.choice(posmovs)
            return action

    def decrement_eps(self):
        self.epsilon = self.epsilon - self.eps_dec if self.epsilon > self.eps_min else self.eps_min

    def store_transition(self, state, action, reward, state_, done):
        self.memory.store_transition(state, action, reward, state_, done)

    def sample_memory(self):
        state, action, reward, new_state, done = \
                                self.memory.sample_buffer(self.batch_size)

        states = torch.tensor(state).to(self.evalnet.device)
        rewards = torch.tensor(reward).to(self.evalnet.device)
        dones = torch.tensor(done).to(self.evalnet.device)
        actions = torch.tensor(action).to(self.evalnet.device)
        states_ = torch.tensor(new_state).to(self.evalnet.device)

        return states, actions, rewards, states_, dones

    def learn(self):
        if self.memory.mem_cntr < self.batch_size:
            return

        self.evalnet.optimizer.zero_grad()

        self.replace_target_network()

        states, actions, rewards, states_, dones = self.sample_memory()
        indices = torch.arange(self.batch_size, device=self.evalnet.device)
        actions = actions-1

        q_pred = self.evalnet.forward(states)[indices, actions.long()]
        q_next = self.nextnet.forward(states_)

        q_next[dones] = 0.0
        q_target = rewards + self.gamma*q_next.max(dim=1)[0]

        loss = self.evalnet.loss(q_target, q_pred).to(self.evalnet.device)
        loss.backward()
        self.evalnet.optimizer.step()
        self.learncounter += 1

        self.decrement_eps()