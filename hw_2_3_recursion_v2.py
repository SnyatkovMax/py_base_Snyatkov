def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('Введите натуральное число >>>  '))
print ('Факториал введенного числа ' + str(n) + ' = ' + str(factorial(n)) ) # вызываем функцию через print