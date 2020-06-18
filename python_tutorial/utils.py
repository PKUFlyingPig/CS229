import matplotlib.pyplot as plt
import random
import numpy as np


def plot(x, y_true, y_pred):

    plt.subplot(2, 1, 1)

    plt.plot(x[y_true == 1][:, 0], x[y_true == 1][:, 1], 'bx', linewidth=2)
    plt.plot(x[y_true == 0][:, 0], x[y_true == 0][:, 1], 'go', linewidth=2)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('True Labels')

    plt.subplot(2, 1, 2)
    plt.plot(x[y_pred == 1][:, 0], x[y_pred == 1][:, 1], 'bx', linewidth=2)
    plt.plot(x[y_pred == 0][:, 0], x[y_pred == 0][:, 1], 'go', linewidth=2) 
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.title('Predicted Labels')

    plt.show()

def generate_data(p, c):
    with open(p, 'w') as f:
        for i in range(c):
            x1 = random.random()
            x2 = random.random()
            y = int(random.random() > 0.5)
            f.write(f'{x1} {x2} {y}\n')

def load_dataset(p):

    with open(p, 'r') as f:
        lines = f.readlines()
    
    all_data = []
    all_y = []
    for l in lines:
        x1, x2, y = l.split()
        x1 = float(x1)
        x2 = float(x2)
        y = int(y)
        all_data.append((x1, x2))
        all_y.append(y)
    
    return np.array(all_data), np.array(all_y)


if __name__ == '__main__':
    generate_data('train_data.txt', 30)