n = 0
while n <= 0:  # повтор, пока n не будет положительным
    n = round(float(input('Введите натуральное число >>> '))) # округляет вещественные числа

factorial = 1
i = 0
while i < n:
     i += 1
     factorial = factorial * i
print ('Факториал введенного числа ' + str(n) + ' = ' + str(factorial) )





