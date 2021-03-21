def function_plus():
    a, b = int(input('> ')), int(input('> '))
    return a + b


def function_minus():
    a, b = int(input('> ')), int(input('> '))
    return a - b


def function_separation():
    a, b = int(input('> ')), int(input('> '))
    return a / b


def function_multiplication():
    a, b = int(input('> ')), int(input('> '))
    return a * b


def function_exponentiation():
    a, n = int(input("> ")), int(input('> '))
    return a ** n


def help_m():
    print('''
                                                𝙼𝚎𝚗𝚞
    :♥: ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ஜ ★ ஜ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ :♥:
                                ★ Q+ENTER - Выход из программы
                                ★ 1 - Вектор по матрице
                                ★ 2 - Вывод коефециентов для уравнения a^2 + b^2 = c^2
                                ★ 3 - Замена элементов матрицы на нули по условию 
                                (Если индекс четный и число пренадлежит списку чисел)
                                ★ 4 -  Рассчет определителя 
                                ★ 5 - ☿ В разроботке!
                                ★ 6 - Формирование бинарного вектора из натурального числа
                                ★ 7 - Формирование списка из списка чисел и строк
                                ★ 8 - Разбитие строки на слова
                                ★ 9 - Проверка на палиндром 
                                ★ 10 - Получение дня недели по дате
    :♥: ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ஜ ★ ஜ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ :♥:
            ''')


help_m()


def menu():
    while (True):
        mod_menu1 = input("Выберите операцию.")
        if mod_menu1 == "q":
            break
        elif mod_menu1 == 'h':
            help_m()
        elif mod_menu1 == '+':
            print(function_plus())
        elif mod_menu1 == '-':
            print(function_minus())
        elif mod_menu1 == '/':
            print(function_separation())
        elif mod_menu1 == '*':
            print(function_multiplication())
        elif mod_menu1 == '**':
            print(function_exponentiation())

        else:
            print('Вы выбрали не сущесвующею операцию')


menu()
