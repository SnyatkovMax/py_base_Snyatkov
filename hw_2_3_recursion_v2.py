def factorial (n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = 0
while n <= 0:  # повтор, пока n не будет положительным
    n = round(float(input('Введите натуральное число >>> '))) # округляет вещественные числа
print ('Факториал введенного числа ' + str(n) + ' = ' + str(factorial(n)) ) # вызываем функцию через print