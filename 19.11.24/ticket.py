num = []
while 1:
    try:
        num = []
        print("\nПриветствую вас в Билетинаторе v0.1")
        print("Чтобы выйти напишите 'exit'")
        inp = str(input("Введите номер билета: "))
        if inp == "exit":
            break
        for i in range(6):
            num.append(inp[i])
        summ1 = int(num[0]) + int(num[1]) + int(num[2])
        summ2 = int(num[3]) + int(num[4]) + int(num[5])
        if summ1 == summ2:
            print("\nВы счастливчик!")
        else:
            print("\nК сожалению в этот раз вам не повезло.")
    except ValueError:
        print("\nОшибка")
    except IndexError:
        print("\nОшибка")

