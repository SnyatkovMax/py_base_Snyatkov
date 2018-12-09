n = 0
while n <= 0:  # повтор, пока n не будет положительным
    n = round(float(input('Введите номер Числа Фибоначчи - n >>>  '))) # округляет введенное число

def fib (n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print ('Элемент ряда Фибоначчи введенного номера ' + str(n) + ' = ' + str(fib(n)) ) # вызываем функцию через print