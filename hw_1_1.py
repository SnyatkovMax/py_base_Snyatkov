name = str(input('Введите имя:  '))
surname = str(input('Введите фамилию:  '))
print('приветствую Вас ' + name + ' ' + surname)
print('------------------------------------------')

born_day = input('Введите день даты рождения:   ')
born_month = input('Введите месяц даты рождения:    ')
born_year = input('Введите год даты рождения:   ')
print('Вы родились  ' + born_day + ' ' + born_month + ' ' + born_year)
print('------------------------------------------')

days = (15+(5*30)) + ((30*12)*29) + ((10*30)+19)
months = int(days / 30)
years = int(months / 12)
print('Вы прожили  ' + str(days) + ' дней, '  + str(months) + ' месяца, '  +  str(years) + ' лет'  + ' до даты начала курса 19.11.2018' )


