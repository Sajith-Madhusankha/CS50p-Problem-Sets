def main():
    time = input("What time is it? ")
    n = convert(time)

    if (7.0 <= n <= 8.0):
        print("breakfast time")
    elif (12 <= n <= 13.0):
        print("lunch time")
    elif (18.0 <= n <= 19.0):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)

    minutes = float(minutes)
    minutes = float(minutes / 60)

    return (hours + minutes)


if __name__ == "__main__":
    main()
