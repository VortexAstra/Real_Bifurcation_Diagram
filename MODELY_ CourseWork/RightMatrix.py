from math import sqrt

from Utils import get_X1, get_P2, get_P3, checkForStationaryPoint, get_X3, checkForPointRotation, findEigenvalues


class RightMatrix:

    @staticmethod
    def solveLowerRight():
        print("Lower-right")
        print("-------------------------------------------------------------------------------------")
        for i in range(61):
            x2 = -1 + 0.05 * i  # For -1 to 2
            x1 = get_X1(x2)
            p2 = get_P2(x2)

            # determinant is zero this is a bifurcation condition and substitute there x3 p3

            a = 57.6 + (1.2 - 1.2 * x1)
            b = -480 * (1 + x1) + 96 * (10 * x1 - x2 + 1) + 48 * (1 - x1)
            c = 40 * pow(10 * x1 - x2 + 1, 2) + 480 * (1 - x1) + 4000 * x1 - 400 * (1 + x1) * (10 * x1 - x2 + 1)

            discriminant = b * b - 4 * a * c
            if discriminant < 0:
                continue
            x4_1 = (-b + sqrt(discriminant)) / (2 * a)
            x4_2 = (-b - sqrt(discriminant)) / (2 * a)

            p3_1 = get_P3(x4_1, x2)
            p3_2 = get_P3(x4_2, x2);
            #
            print("\033[31m")
            # print(p3_1)
            print("x1 = ", x1, ", x2 = ", x2, ", x4 = ", x4_1, ", p2 = ", p2, ", p3 = ", p3_1)
            checkForStationaryPoint(x1, x2, get_X3(x4_1, x2), x4_1, p2, p3_1)
            checkForPointRotation(x2, x4_1)
            findEigenvalues(x2, x4_1)
            print("\033[33m")
            # print(p3_2)
            print("x1 = ", x1, ", x2 = ", x2, ", x4 = ", x4_2, ", p2 = ", p2, ", p3 = ", p3_2)
            checkForStationaryPoint(x1, x2, get_X3(x4_2, x2), x4_2, p2, p3_2)
            checkForPointRotation(x2, x4_2)
            findEigenvalues(x2, x4_2)
