
import math

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        def side_len(top_1, top_2):
            return math.sqrt((top_1[0] - top_2[0]) ** 2 + (top_1[1] - top_2[1]) ** 2)

        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CA = side_len(self.C, self.A)

    def triangle_p(self):
        return self.AB + self.BC + self.CA

    def triangle_s(self):
        half_p = self.triangle_p() / 2
        return math.sqrt(half_p * (half_p - self.AB) * (half_p - self.BC) * (half_p - self.CA))

    def triangle_h(self):
        return self.triangle_s() / (self.AB / 2)

treugolnik_1 = Triangle((3, 2), (6, 7), (0, 12))

print(treugolnik_1.triangle_s())
print(treugolnik_1.triangle_h())
print(treugolnik_1.triangle_p())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, A, B, C, D):
        # Функция вычисляет длину стороны согласно координатам точек
        def side_len(top_1, top_2):
            return math.sqrt((top_1[0] - top_2[0]) ** 2 + (top_1[1] - top_2[1]) ** 2)

        def triangle_s(len_1, len_2, len_3):
            half_p = (len_1 + len_2 + len_3) / 2

            return math.sqrt(half_p * (half_p - len_1) * (half_p - len_2) * (half_p - len_3))

        self.A = A
        self.B = B
        self.C = C
        self.D = D

        self.AB = side_len(self.A, self.B)
        self.BC = side_len(self.B, self.C)
        self.CD = side_len(self.C, self.D)
        self.DA = side_len(self.D, self.A)
        self.diagonal_AC = side_len(self.C, self.A)
        self.diagonal_BD = side_len(self.B, self.D)

        self.p = self.AB + self.BC + self.CD + self.DA
        self.s = triangle_s(self.AB, self.diagonal_BD, self.DA) + triangle_s(self.diagonal_BD, self.BC, self.CD)

    def isTrapeze(self):
        if self.diagonal_AC == self.diagonal_BD:
            return True
        return False