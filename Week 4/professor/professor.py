import random
import sys


def main():
    stage = 0
    score = 0
    tries = 3
    level = get_level()

    while stage != 10:
        if tries == 3:
            x, y = generate_integer(level)
        try:
            user_input = int(input(f"{x} + {y} = "))
            answer = x + y
            if user_input == answer:
                stage += 1
                score += 1
                tries = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print("EEE")
            tries -= 1
            pass
        if tries == 0:
            print(f"{x} + {y} = {answer}")
            tries = 3
            stage += 1
            continue

        print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    else:
        raise ValueError
    return x, y


if __name__ == "__main__":
    main()