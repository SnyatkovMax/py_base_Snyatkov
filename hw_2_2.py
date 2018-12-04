m = int(input("Введите натуральное число: "))
n = int(input("Введите еще одно натуральное число: "))

if m > n:
    m,n = n,m

for x in range(m, n+1, 1):
    print('i =', x)

my_range = range(m, n+1, 1)
print('сумма всех натуральных чисел в заданом диапазоне =', sum(my_range))




