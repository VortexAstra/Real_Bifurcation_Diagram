import math

from Utils import get_P2


class LeftMatrix:
    @staticmethod
    def solveUpperLeft():
        print("Left")
        print("-------------------------------------------------------------------------------------");
        # Получил квадратное(x2) 49х^2 - 280x + 100 = 0
        a = 49
        b = -280
        c = 100

        discriminant = b * b - 4 * a * c
        sqrtD = math.sqrt(discriminant)

        x2_1 = (-b + sqrtD) / (2 * a)
        x2_2 = (-b - sqrtD) / (2 * a)

        print("X2_1", x2_1, "X2_2", x2_2)

        p2_1 = get_P2(x2_1)
        p2_2 = get_P2(x2_2)

        print("P2_1", p2_1, "P2_2", p2_2)
