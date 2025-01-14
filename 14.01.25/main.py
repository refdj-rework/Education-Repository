import pandas as pd
data = pd.read_excel('data.xlsx')
def co_str():
    a = int(input("Введите номер столбца: "))
    b = int(input("Введите номер строки: "))
    print(data.iloc[a, b])
    passs = input("Нажмите ENTER чтобы продолжить...")

while 1:
    try:
        print("Выберите одно из перечисленных: 'ячейка', 'столбец', 'строка'.")
        print("Чтобы вывести всю таблицу используйте 'таблица'.")
        inp = str(input("Ввод: "))
        post_inp = inp.lower()
        if post_inp == "ячейка":
            co_str()
        elif post_inp == "столбец":
            a = int(input("Введите номер столбца: "))
            print(data.iloc[a, :])
            passs = input("Нажмите ENTER чтобы продолжить...")
        if post_inp == "строка":
            b = int(input("Введите номер строки: "))
            print(data.iloc[:, b])
            passs = input("Нажмите ENTER чтобы продолжить...")

    except ValueError:
        print("xD")