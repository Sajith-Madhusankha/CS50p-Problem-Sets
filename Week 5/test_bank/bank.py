def main():
    greeting = input("Greeting: ").lower().strip()
    x = value(greeting)
    print(f"${x}")


def value(greeting):
    if greeting.startswith("hello"):
        x = 0
    elif greeting.startswith("h"):
        x = 20
    else:
        x = 100
    return x


if __name__ == "__main__":
    main()