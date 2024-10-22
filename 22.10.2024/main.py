import sys
def division(a,b):
    try:
        rep = a / b
    except ZeroDivisionError:
        rep = 0
    except SyntaxError:
        print("Ошибка синтаксиса!")
    except ValueError:
        print("Некорректное значение!")
    print(rep)

def multiplication(a,b):
    try:
        rep = a * b
    except SyntaxError:
        print("Ошибка синтаксиса!")
    except ValueError:
        print("Некорректное значение!")
    print(rep)

def subtraction(a,b):
    try:
        rep = a - b
    except SyntaxError:
        print("Ошибка синтаксиса!")
    except ValueError:
        print("Некорректное значение!")
    print(rep)

def summ(a,b):
    try:
        rep = a + b
    except SyntaxError:
        print("Ошибка синтаксиса!")
    except ValueError:
        print("Некорректное значение!")
    print(rep)

while(True):
    num1 = 0
    num2 = 0
    operation = ""
    while(operation != "+" and operation != "-" and operation != "/" and operation != "*" and operation != "exit"):
        print("       ")
        print("       ")
        print("       ")
        print("+ - / *")
        print("Если хочешь выйти из программы напиши 'exit'")
        operation = str(input("Введите операцию: "))
        if operation != "+" and operation != "-" and operation != "/" and operation != "*" and operation != "exit":
            print("Ваш ввод некорректный!")
        elif operation == "exit" or operation == "EXIT":
            sys.exit()

    try:
        num1 = float(input("Первое число: "))
        num2 = float(input("Второе число: "))
    except ValueError:
        print("Некорректное значение!")
    except SyntaxError:
        print("Некорректное значение!")

    if operation == "/":
        division(num1,num2)

    elif operation == "*":
        multiplication(num1,num2)

    elif operation == "-":
        subtraction(num1, num2)

    elif operation == "+":
        summ(num1, num2)
    enter_flag = input("Нажми ENTER тобы продолжить...")


