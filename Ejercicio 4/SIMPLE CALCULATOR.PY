def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def show_menu():
    print("1. Add")
    print("2. subtract")
    print("3. multiplication")
    print("4. division")
    print("5. exit")

def calculator():
    show_menu()

    number1 = int(input("Enter a number to calculate: "))
    number2 = int(input("Enter a number to calculate: "))

    option = int(input("Enter a opction: "))

    if option == 1:
        print(add(number1, number2))
        return False
    elif option == 2:
        print(subtract(number1, number2))
        return False
    elif option == 3:
        print(multiplication(number1, number2))
        return False
    elif option == 4:
        print(division(number1, number2))
        return False
    elif option == 5:
        print("Goodbye!!!")
        return True
    else:
        print("Invalid option!!")
        return False

def run():
    exit = False
    while not exit:
        exit = calculator()

run()