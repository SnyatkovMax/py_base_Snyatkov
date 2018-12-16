def add(a, b):  # функция сложения
    return a + b


def sub(a, b):  # функция вычитания
    return a - b


def mult(a, b):  # функция умножения
    return a * b


def div(a, b):  # функция деления
    try:
        return a / b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def int_div(a, b):  # функция целочисленного деления
    try:
        return a // b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def ostatok_ot_div(a, b):  # функция остатка от деления
    try:
        return a % b
    except ZeroDivisionError as err:
        print('Ошибка при делении на 0 >>>', err)


def exponentiation(a, b):  # функция возведение в степень
    return a ** b


def start_program():  # функция входа в калькулятор
    start = input('Для запуска калькулятора введите: 1, для выхода введите что угодно >>>   ')
    if start == '1':
        print('приступим к работе')
    else:
        print('конец программы')
        exit()


calculator = {  # возможные операции калькулятора
    '+': add,
    '-': sub,
    '*': mult,
    '/': div,
    '//': int_div,
    '%': ostatok_ot_div,
    '**': exponentiation
}

start_program()  # вход в программу

while True:  # циклический ввод данных от пользователя
    try:
        print('Возможные операции данного калькулятора: ', list(calculator.keys()))
        a = float(input('введите первое число >>> '))
        operation = input('введите операцию >>> ').strip()
        b = float(input('введите второе число >>> '))
    except ValueError as error:
        print('Ошибка ввода:', error)
        print('Попробуйте еще раз ')
        print()
    except Exception as err:
        print('Ошибка:', err)
    else:
        break

result = None

if operation in list(calculator.keys()):
    result = calculator[operation](a, b)

if result is not None:
    print('Результат операции = ', result)
