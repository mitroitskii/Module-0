import random
from dataclasses import dataclass


def make_pts(N):
    X = []
    for i in range(N):
        x_1 = random.random()
        x_2 = random.random()
        X.append((x_1, x_2))
    return X


@dataclass
class Graph:
    N: int
    X: list
    y: list


# FIXME: doc
# Current hypothesis – y is just a bit, signifying a label (i.e. whether the point is X or O)
def simple(N):
    # create a list of tuples of length N
    X = make_pts(N)
    # y is a list of labels
    labels = []
    for x_1, x_2 in X:
        # if the point lies before the middle on the x-axis, it's an X, otherwise it's O
        label = 1 if x_1 < 0.5 else 0
        labels.append(label)
    return Graph(N, X, labels)


def diag(N):
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 + x_2 < 0.5 else 0
        y.append(y1)
    return Graph(N, X, y)


def split(N):
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if x_1 < 0.2 or x_1 > 0.8 else 0
        y.append(y1)
    return Graph(N, X, y)


def xor(N):
    X = make_pts(N)
    y = []
    for x_1, x_2 in X:
        y1 = 1 if ((x_1 < 0.5 and x_2 > 0.5) or (x_1 > 0.5 and x_2 < 0.5)) else 0
        y.append(y1)
    return Graph(N, X, y)


datasets = {"Simple": simple, "Diag": diag, "Split": split, "Xor": xor}
