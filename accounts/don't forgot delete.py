N = 7


# здесь задается функция fib_rec (переменную N не менять!)
def fib_rec(N, f=[1, 1]):
    if N == 2:
        return f
    return fib_rec(N - 1, f.append(f[-2] + f[-1]))


print(fib_rec(N))
