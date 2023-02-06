# объявление функции
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    return sorted(((-b - d ** 0.5) / (2 * a), (-b + d ** 0.5) / (2 * a)), key=int)
# считываем данные


# вызываем
x1, x2 = solve(-2, 7, -5)

print(x1, x2)
