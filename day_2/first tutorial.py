import numpy as np
import matplotlib.pyplot as plt


def first():
    x = 2 * np.random.rand(100, 1)
    y = 4 + 3 * x + np.random.randn(100, 1)
    plt.scatter(x, y)
    plt.xlabel("x1")
    plt.ylabel("Y")
    plt.show()
    return x, y

# x_b (100, 2) (2, 100)
# (100, 100) (100, 2) --> (2, 100) (100, 1) --> (2, 1)
# y (100, 1)

def second(x, y):
    x_b = np.c_[np.ones((100, 1)), x]
    print(y.shape)
    best_theta = (np.linalg.inv(x_b.dot(x_b.T)).dot(x_b)).T.dot(y)

    print(best_theta)
    return best_theta


def predictor(best_theta):
    x_new = np.array([[0], [2]])
    x_new_b = np.c_[np.ones((2, 1)), x_new]  # adds xθ to each instance
    y_predict = x_new_b.dot(best_theta)
    print(y_predict)
    return x_new, y_predict


def plotter(x, y, x_new, y_predict):
    plt.plot(x_new, y_predict, "r-")
    plt.plot(x, y, "b")
    plt.axis([0, 2, 0, 15])
    plt.show()


def shut_down():
    import shutdown
    shutdown.shutdown()


if __name__ == '__main__':
    x, y = first()
    # print(x, )
    best_theta = second(x, y)
    x_new, y_predict = predictor(best_theta)
    plotter(x, y, x_new, y_predict)
