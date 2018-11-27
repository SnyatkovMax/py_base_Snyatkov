num1 = int(input('Введите целое число num1:  '))
num2 = int(input('Введите еще одно целое число num2:  '))


print('Вывод числа num1 в представлении целого числа, вещественного числа, логического значения, строки')
print(num1) # выведет целое число
print(float(num1)) # выведет вещественное число
print(bool(num1)) # выведет булево значение
print(str(num1)) # введенное число из int переведет в str и выведет тоже самое

print('результат допустимых операций + над всеми вариантами представления num1 и num2')
print(num1 + num2)
print(num1 + float(num2))
print(num1 + bool(num2))
#print(num1 + str(num2)) - выведет ошибку
print('------------------------------------------')

print(float(num1) + num2)
print(float(num1) + float(num2))
print(float(num1) + bool(num2))
#print(float(num1) + str(num2)) - выведет ошибку
print('------------------------------------------')

print(bool(num1) + num2)
print(bool(num1) + float(num2))
print(bool(num1) + bool(num2))
#print(bool(num1) + str(num2)) - выведет ошибку
print('------------------------------------------')

#print(str(num1) + num2) - выведет ошибку
#print(str(num1) + float(num2)) - выведет ошибку
#print(str(num1) + bool(num2)) - выведет ошибку
print(str(num1) + str(num2)) # прибавляет строку к строке
print('------------------------------------------')

print('результат допустимых операций * над всеми вариантами представления num1 и num2')
print(num1 * num2)
print(num1 * float(num2))
print(num1 * bool(num2))
print(num1 * str(num2))
print('------------------------------------------')

print(float(num1) * num2)
print(float(num1) * float(num2))
print(float(num1) * bool(num2))
#print(float(num1) * str(num2)) - выведет ошибку
print('------------------------------------------')

print(bool(num1) * num2)
print(bool(num1) * float(num2))
print(bool(num1) * bool(num2))
print(bool(num1) * str(num2))
print('------------------------------------------')

print(str(num1) * num2)
#print(str(num1) * float(num2)) - выведет ошибку
print(str(num1) * bool(num2))
#print(str(num1) * str(num2)) - выведет ошибку
