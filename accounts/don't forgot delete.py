l = ['8', '11', '-5', '4', '3']


def get_rec_sum(l):
    print('i')
    if len(l) == 1:
        return +int(l[0])
    return int(l[0]) + get_rec_sum(l[1:])


num = get_rec_sum(l)
print(num)
a = 5
b = 10

a, b = b, a