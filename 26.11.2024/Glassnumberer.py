while(1):
    try:
        flag = 0
        voice =  str('аеёиоуыэюя')
        print("Для выхода используйте 'exit'")
        inp = str(input("Введите буквы: "))
        inp = inp.lower()
        inp = inp.strip()
        for i in range(0, len(inp)):
            check = inp[i:i + 1]
            for j in range(0, len(voice)):
                rep = voice[j] in check
                #print(voice[j], rep, i, j)
                if rep == True:
                    flag += 1
                    break
        print(f"Количество гласных: {flag}")
        enter = input("Нажмите ENTER чтобы продолжить...")
        if inp == "exit":
            break
    except(ValueError):
        print("Ошибка!")
    except(IndexError):
        print("Ошибка!")
