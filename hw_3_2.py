def sort_words():
    print('Программа для сортировки слов из текста')
    my_count = input('Введите слова >>> ').lower().replace(',', ' ')
    if my_count.isspace():
        print('Слово не введено, программа завершена')
        quit()
    else:
        pass
    res = sorted(list(my_count.split()))
    print(res)


sort_words()
