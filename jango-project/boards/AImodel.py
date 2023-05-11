import numpy as np
import torch
from torch import nn

np.set_printoptions(formatter={'float': lambda x: "{0:0.6f}".format(x)})

class statistical(nn.Module):
    def __init__(self, input_dim=7, hidden_dim=128, seq_len=100, output_dim=7, layers=1, p=0.3):
        super(statistical, self).__init__()
        self.input_dim = input_dim
        self.hidden_dim = hidden_dim
        self.seq_len = seq_len
        self.output_dim = output_dim
        self.layers = layers
        self.p = p
        self.lstm = nn.LSTM(self.input_dim, self.hidden_dim, num_layers=self.layers, batch_first=True)
        self.fc = nn.Linear(self.hidden_dim*self.layers, self.output_dim, bias=True)
        self.softmax = nn.Softmax(dim=1)
        self.softmin = nn.Softmin(dim=1)

    def reset_hidden_state(self):
        self.hidden = (torch.zeros(self.layers, self.seq_len, self.hidden_dim),
                       torch.zeros(self.layers, self.seq_len, self.hidden_dim))

    def forward(self, inputs):
        outputs, _status = self.lstm(inputs)
        outputs = self.fc(outputs[:, -1])  # 맨 마지막 값만
        prob = np.random.uniform()
        if prob < self.p:
            outputs = self.softmin(outputs)
        else:
            outputs = self.softmax(outputs)

        return outputs
