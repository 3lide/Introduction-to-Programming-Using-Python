import math

class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDescriminant(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRoot1(self):
        if self.getDescriminant() >= 0:
            return (-self.__b + math.sqrt(self.getDescriminant())) / (2 * self.__a)
        else:
            return 0

    def getRoot2(self):
        if self.getDescriminant() >= 0:
            return (-self.__b - math.sqrt(self.getDescriminant())) / (2 * self.__a)
        else:
            return 0
