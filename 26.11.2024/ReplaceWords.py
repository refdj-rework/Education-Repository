while 1:
    try:
        print("\nДля выхода напишите 'exit'")
        inp = str(input("Ввежите свои буквы: "))
        split = inp.split(" ")
        for i in range(0, len(split)):
            split.insert(0, split.pop(i))
        print(split)
        passs = input("Нажмите ENTER для продолжения...")
        if inp == "exit":
            break
    except(ValueError):
        print("Ошибка!")
    except(TypeError):
        print("Ошибка!")
    except(IndexError):
        print("Ошибка!")
