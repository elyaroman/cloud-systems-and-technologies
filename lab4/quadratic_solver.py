import math

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент 'a' не может быть равен нулю.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "Нет действительных корней"

    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)

    return x1, x2
