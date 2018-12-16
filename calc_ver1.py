def add(a, b):
    return a + b

def min(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Division by zero detected')
    #return a / b









calc = {
    '+': add,
    '-': min,
    '*': mult,
    '/': div
}


print('Возможные операции данного калькулятора: ', list(calc.keys()))






a = float(input('введите первое число >>> '))
operation = input('operation ').strip()
b = float(input('введите второе число >>> '))






result = None

if operation in list(calc.keys()):
    result = calc[operation](a, b)


if result is not None:
    print('Результат операции = ', result)



