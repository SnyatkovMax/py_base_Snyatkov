n = int(input('Введите номер Числа Фибоначчи - n >>>  '))

a = 1
b = 1
i = 2
while i < n:
    sum = b + a
    a = b
    b = sum
    i += 1

print ('Элемент ряда Фибоначчи введенного номера ' + str(n) + ' = ' + str(sum) )