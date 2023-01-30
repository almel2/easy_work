def get_next_prime(num):
    count = 0
    for i in range(1, num*2):
        if i % 1 == 0 and i % i == 0:
            count += 1
        if count == 2 and i > num:

            print(i, i % num)
            return(i)


# считываем данные
n = 7

# вызываем функцию
print(get_next_prime(n))

print(7 % 7)