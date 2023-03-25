while True:
    try:
        calculator = ('+', '-', '//', '*')
        questions = input("Напишите (+-//*): ")
        if questions == "quit":
            break
        elif questions not in calculator:
            print("Вы ввели неккоректный знак")
        else:
            first = int(input("Первое число: "))
            if first == "quit":
                break
            last = int(input("Второе число: "))
            if last == "quit":
                break
            if questions == "+":
                adition = int(first) + int(last)
                print(adition)
            elif questions == "-":
                subtraction = int(first) - int(last)
                print(subtraction)
            elif questions == "//":
                division = int(first) // int(last)
                print(division)
            elif questions == "*":
                multiplications = int(first) * int(last)
                print(multiplications)
    except ValueError:
        print("Вы написали текст. Попробуйте заново")