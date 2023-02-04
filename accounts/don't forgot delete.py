# объявление функции
def is_password_good(password):
    counter = 0
    if len(password) < 8:
        return False
    for i in password:
        if i.islower():
            counter += 1
            break
    for i in password:
        if i.isupper():
            counter += 1
            print(i)
            break
    for i in password:
        if i.isdigit():
            counter += 1
            break
    if counter == 3:
        return True
    return False


# считываем данные
txt = 'dsas233232232'

# вызываем функцию
print(is_password_good(txt))

