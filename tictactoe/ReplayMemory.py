import numpy as np

class ReplayBuffer():
    def __init__(self, memorysize, statespace):
        self.memorysize = memorysize
        self.mem_cntr = 0

        self.state_memory = np.zeros([self.memorysize, statespace.shape[0], statespace.shape[1]], dtype=np.float32)
        self.new_state_memory = np.zeros([self.memorysize, statespace.shape[0], statespace.shape[1]], dtype=np.float32)

        self.action_memory = np.zeros(self.memorysize, dtype=np.int8)
        self.reward_memory = np.zeros(self.memorysize, dtype=np.float32)
        self.terminal_memory = np.zeros(self.memorysize, dtype=np.bool)

    def store_transition(self, state, action, reward, state_, done):
        index = self.mem_cntr % self.memorysize
        self.state_memory[index] = state
        self.new_state_memory[index] = state_
        self.action_memory[index] = action
        self.reward_memory[index] = reward
        self.terminal_memory[index] = done
        self.mem_cntr += 1

    def sample_buffer(self, batch_size):
        max_mem = min(self.mem_cntr, self.memorysize)
        batch = np.random.choice(max_mem, batch_size, replace=False)

        states = self.state_memory[batch]
        actions = self.action_memory[batch]
        rewards = self.reward_memory[batch]
        states_ = self.new_state_memory[batch]
        terminal = self.terminal_memory[batch]
        return states, actions, rewards, states_, terminal
