name = input('Введите имя:  ')
surname = input('Введите фамилию:  ')
print('приветствую Вас ' + name + ' ' + surname)
print('------------------------------------------')

born_day = int(input('Введите день даты рождения:   '))
born_month = int(input('Введите месяц даты рождения:    '))
born_year = int(input('Введите год даты рождения:   '))
m = 30
years = 2018 - born_year
months = (12 - born_month) + ( (years - 1) * 12) + 10
days = ( (  (12 - born_month) * m)  +  (m - born_day) )  + ( (years - 1) * 12 * m) + (m * 10) + 19


print('Вы родились  ' + str(born_day) + ' ' + str(born_month) + ' ' + str(born_year) )

print('Вы прожили  ' + str(days) + ' дней, '  + str(months) + ' месяца, '  +  str(years) + ' лет'  + ' до даты начала курса 19.11.2018' )


