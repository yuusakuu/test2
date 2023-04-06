import numpy as np



def train_test(train, test):
    train = train.to_numpy()
    test = test.to_numpy()
    return train, test



def convert_to_matrix(data, step):
    x, y = [], []
    for i in range(len(data) - step):
        d = i + step  
        x.append(data[i:d])
        y.append(data[d])
    return np.array(x), np.array(y)


def reshape(train_x, test_x):
    train_x = np.reshape(train_x, (train_x.shape[0], 1, train_x.shape[1]))
    test_x = np.reshape(test_x, (test_x.shape[0],1,  test_x.shape[1]))
    return train_x, test_x