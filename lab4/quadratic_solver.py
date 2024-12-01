import math

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    :param a: коэффициент при x^2
    :param b: коэффициент при x
    :param c: свободный член
    :return: кортеж из двух корней (x1, x2) или сообщение об отсутствии решений
    """
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "Нет действительных корней"

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return x1, x2
