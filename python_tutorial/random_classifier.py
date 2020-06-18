import random
import numpy as np
import utils


class RandomClassifier:

    def __init__(self, bias_prob):
        self.bias_prob = bias_prob
        self.pred_prob = 0

    def fit(self, x, y):
        data_ratio = len(y[y == 1]) / len(y)
        self.pred_prob = data_ratio + self.bias_prob

    def predict(self, x):

        pred_labels = []
        for i in range(len(x)):
            r = random.random()
            label = 1 if r > self.pred_prob else 0
            pred_labels.append(label)
        
        return np.array(pred_labels)


def main(train_path, test_path):

    train_x, train_y = utils.load_dataset(train_path)
    test_x, test_y = utils.load_dataset(test_path)

    classifier = RandomClassifier()
    classifier.fit(train_x, train_y)

    test_pred_y = classifier.predict(test_x)
    utils.plot(test_x, test_y, test_pred_y)


if __name__ == '__main__':
    main('train_data.txt', 'test_data.txt')