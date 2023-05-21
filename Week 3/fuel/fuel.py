while True:
    try:
        text = input("Fraction: ")
        x, y = text.split("/")
        x = int(x)
        y = int(y)

        while x > y:
            text = input("Fraction: ")
            continue

        percentage = float(x / y)

    except (ValueError, ZeroDivisionError):
        pass

    else:

        if 0.99 <= percentage <= 1:
            print("F")
        elif 0.01 >= percentage >= 0:
            print("E")
        elif 0.01 < percentage < 0.99:
            print(f"{round(percentage * 100)}%")
        else:
            pass
        break

