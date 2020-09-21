import numpy as np
import torch.nn as nn
import torch.nn.functional as f
import torch
class DQNet(nn.Module):
    def __init__(self, lr, statespace, actionspace, chkpt_dir):
        super(DQNet, self).__init__()
        self.lr = lr
        self.statespace = statespace
        self.actionspace = actionspace
        self.chkpt_dir = chkpt_dir

        self.conv1 = torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=2)
        self.conv2 = torch.nn.Conv2d(in_channels=16, out_channels=32, kernel_size=2)
        self.fc1 = nn.Linear(self.calc_fcsize(statespace=statespace), 256)
        self.fc2 = nn.Linear(256, self.actionspace)

        self.optimizer = torch.optim.Adadelta(self.parameters(), lr=self.lr, )
        self.loss = nn.MSELoss()
        self.device = torch.device("cpu" if torch.cuda.is_available() else "cpu")
        self.to(self.device)

    def forward(self, x):
        x = x.unsqueeze(1)
        x = f.tanh(self.conv1(x))
        x = f.tanh(self.conv2(x))
        x = x.squeeze()
        x = self.fc1(x)
        x = self.fc2(x)
        x = f.relu(x)
        return x

    def calc_fcsize(self, statespace):
        test = torch.zeros(1, 1, *statespace.shape)
        test = self.conv1(test)
        test = self.conv2(test)
        fcchannels = int(np.prod(test.size()))
        return fcchannels

    def save_checkpoint(self):
        print("saving state-dict...")
        torch.save(self.state_dict(), self.chkpt_dir)

    def load_checkpoint(self):
        print("loading state-dict...")
        self.load_state_dict(torch.load(self.chkpt_dir))