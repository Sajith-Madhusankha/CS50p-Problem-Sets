def main():
    text = input("Fraction: ")
    percentage = convert(text)
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    m, n = int(x), int(y)
    if m / n > 1:
        raise ValueError
    elif int(n) == 0:
        raise ZeroDivisionError
    return (m/n * 100)


def gauge(percentage):
    try:
        if 99 <= percentage <= 100:
            return "F"
        elif 1 >= percentage >= 0:
            return "E"
        elif 1 < percentage < 99:
            return f"{round(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()