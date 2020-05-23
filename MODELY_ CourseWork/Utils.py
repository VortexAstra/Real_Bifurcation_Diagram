from math import exp

import numpy as np

N = 4


def get_X1(x2):
    return (1.2 * x2 + 1) / 10


def get_P2(x2):
    x1 = get_X1(x2)
    return x1 / ((1 - x1) * exp(x2 / (1 + x2 / 20)))


def get_X3(x4, x2):
    x1_c = get_X1(x2)
    return (1.2 * x4 + 10 * x1_c - x2 + 1) / 10


def get_P3(x4, x2):
    x1_c = get_X1(x2)
    x3_c = get_X3(x4, x2)
    return (x3_c - x1_c) / ((1 - x3_c) * exp(x4 / (1 + x4 / 20)))


def checkForStationaryPoint(x1, x2, x3, x4, p2, p3):
    nums = [1, 2, 3, 4]
    nums[0] = -x1 + p2 * (1 - x1) * exp(x2 / (1 + x2 / 20))
    nums[1] = -x2 + p2 * 10 * (1 - x1) * exp(x2 / (1 + x2 / 20)) - 0.2 * (x2 + 5)
    nums[2] = (x1 - x3 + p3 * (1 - x3) * exp(x4 / (1 + x4 / 20))) * p2 / p3
    nums[3] = (x2 - x4 + p3 * 10 * (1 - x3) * exp(x4 / (1 + x4 / 20)) - 0.2 * (x4 + 5)) * p2 / p3

    for i in range(N):
        if abs(nums[i]) > 1E-12:
            print("Not stationary")
    print("It is a stationary point")


def checkForPointRotation(x2, x4):
    x1 = get_X1(x2)
    p2 = get_P2(x2)
    x3 = get_X3(x4, x2)
    p3 = get_P3(x4, x2)
    arr = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

    arr[0][0] = -1 - p2 * exp(x2 / (1 + x2 / 20))
    arr[1][0] = -10 * p2 * (x2 / (1 + x2 / 20))
    arr[1][1] = -1.2 + p2 * 4000 * (1 - x1) * (x2 / (1 + x2 / 20)) / pow(20 + x2, 2)
    arr[0][1] = p2 * 400 * (1 - x1) * (x2 / (1 + x2 / 20)) / pow(20 + x2, 2)

    arr[2][2] = -p2 / p3 - p2 * (x4 / (1 + x4 / 20))
    arr[2][3] = -p2 * (x1 - x3) * (1 / p3) * (1 / p3)
    arr[3][2] = -10 * p2 * (x4 / (1 + x4 / 20))
    arr[3][3] = p2 * (x2 - x4 - 0.2 * (x4 + 5)) * (1 / p3) * (1 / p3)  # производная по p3

    d1 = arr[0][0] * arr[1][1] - arr[0][1] * arr[1][0]
    d2 = arr[2][2] * arr[3][3] - arr[2][3] * arr[3][2]

    d = d1 * d2
    if abs(d) > 1E-9: # не должно быть (условие точки поворота)!= нулю
        print(d)
        # print("Det = ", d, "=> Point Rotation")


def findEigenvalues(x2, x4):
    x1 = get_X1(x2)
    p2 = get_P2(x2)
    x3 = get_X3(x4, x2)
    p3 = get_P3(x4, x2)

    matrix = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    matrix[0][0] = -1 - p2 * exp(x2 / (1 + x2 / 20))
    matrix[0][1] = p2 * 400 * (1 - x1) * (x2 / (1 + x2 / 20)) / pow(20 + x2, 2)
    matrix[0][2] = 0
    matrix[0][3] = 0

    matrix[1][0] = -10 * p2 * exp(x2 / (1 + x2 / 20))
    matrix[1][1] = -1.2 + p2 * 4000 * (1 - x1) * exp(x2 / (1 + x2 / 20)) / pow(20 + x2, 2)
    matrix[1][2] = 0
    matrix[1][3] = 0

    matrix[2][0] = p2 / p3
    matrix[2][1] = 0
    matrix[2][2] = -p2 / p3 - p2 * exp(x4 / (1 + x4 / 20))
    matrix[2][3] = p2 * 400 * (1 - x3) * exp(x4 / (1 + x4 / 20)) / pow(20 + x4, 2)

    matrix[3][0] = 0
    matrix[3][1] = p2 / p3
    matrix[3][2] = -10 * p2 * exp(x4 / (1 + x4 / 20))
    matrix[3][3] = -1.2 * (p2 / p3) + p2 * 4000 * (1 - x3) * exp(x4 / (1 + x4 / 20)) / pow(20 + x4, 2)

    w, v = np.linalg.eig(matrix)
    print(w)

    negative = False
    positive = False

    for element in w:
        if element < 0:
            negative = True
        if element > 0:
            positive = True
        if element == 0:
            positive = True
            negative = True

    if negative and positive:
        print("\033[34m Вещественная бифуркация")


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_blue(text):
    print("\033[34m {}".format(text))
