import random
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from torch.autograd import Variable
from torchvision import datasets, transforms


def get_hyp():
    seed = 123
    data_dim = 7
    # seq_length = 100
    seq_length = 30
    hidden_dim = 128  # hidden layer dimension
    output_dim = data_dim
    learning_rate = 1e-2
    epochs = 100
    batch_size = 50
    probability = 0.3

    return seed, data_dim, seq_length, hidden_dim, output_dim, learning_rate, epochs, batch_size, probability


def on_device():
    # 디바이스

    device = ('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'device : {device}')
    return device


def make_data(data_dim=7, SEED=123, data=None, new=None):
    # 데이터 생성
    if not new:
        random.seed(SEED)  # torchvision seed
        np.random.seed(SEED)  # numpy ndarray seed
        torch.manual_seed(SEED)  # torch tensor seed
        torch.cuda.manual_seed(SEED)  # torch cuda seed
        torch.cuda.manual_seed_all(SEED)  # torch cuda multi-gpu seed
        # newdata = torch.eye(data_dim, dtype=torch.float32, requires_grad=False)[np.random.choice(data_dim, 300)]
        newdata = torch.eye(data_dim, dtype=torch.float32, requires_grad=False)[np.random.choice(data_dim, 100)]

        return newdata

    newvector = torch.zeros(size=(1, data_dim))
    newvector[0][new-1] += 1.  # -1 하는 이유는, 선택지가 1부터 시작하기 때문이다.
    newdata = torch.concat((data[1:],newvector))

    return newdata


def seq_data(sequences, window=100, data_dim=7, batch_size=50):  # sequences에는 위에서 나오는 newdata를 그대로 넣으면 되며, window=seq_length이다. batchsize는 dataloader때문에 내가 추가한거니까, 헷갈리지 말자.
    # 데이터 나누기
    # feature_tensor = 0
    for i in range(len(sequences) - window):
        if i == 0:
            feature_tensor = sequences[i:i + window].clone().detach().reshape(1, window, data_dim)
            label_tensor = sequences[i + window].clone().detach().reshape(1, data_dim)
        else:
            feature_tensor = torch.cat((feature_tensor, sequences[i:i + window].reshape(1, window, data_dim)), 0)
            label_tensor = torch.cat((label_tensor, sequences[i + window].reshape(1, data_dim)), 0)  # one-hot vector 형식
    # print(sequences.shape, feature_tensor.shape, label_tensor.shape)
        # label_list.append(np.where(sequences[i+window]==1)[0])  # value 형식
    dataloader = DataLoader(TensorDataset(feature_tensor, label_tensor), batch_size=batch_size, shuffle=False, drop_last=True)
    return dataloader  # X와 y를 합친 텐서데이터로더 자체를 리턴. 이걸로 모델 트레이닝에 넣으면 된다.


def train_model(model, dataloader, epochs=100, lr=1e-2, patience=10, device=None):
    # train

    model.train()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.RMSprop(model.parameters(), lr=lr)
    history = np.zeros(epochs)

    for epoch in range(epochs):
        avg_cost = 0
        total_batch = len(dataloader)

        for batch_idx, batchs in enumerate(dataloader):
            X, y = batchs
            X.to(device)
            y.to(device)
            model.reset_hidden_state()  # 이거 지워보고 유의미한 차이가 나는지 실험해보기

            outputs = model(X)
            loss = criterion(outputs, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            avg_cost += loss / total_batch

        history[epoch] = avg_cost

        # if (epoch!=0) and (epoch%patience==0):  # early stopping은 나중에 보고 결정하기 왜냐하면 뒤의 예측에서 물흘러가듯이 흘러가다가 마지막 값을 쓰고 싶기 때문에
        #     if history[epoch-patience] < history[epoch]:
        #         print('\n early stop')
        #         break
    model.eval()
    newX = torch.concat((X[-1][1:],y[-1:]))
    newXX = newX.reshape(1,newX.shape[0],newX.shape[1])
    newXX = model(newXX)
    # print('예측', newXX.shape, model(newXX))

    return model, np.argmax(newXX.cpu().detach().numpy())+1  # 왼쪽의 eval은 tf처럼 점수를 보겠단 뜻이 아니라, train모드와 eval모드로 전환시킨다는 뜻이다. 결국에는 모델 그 자체임.