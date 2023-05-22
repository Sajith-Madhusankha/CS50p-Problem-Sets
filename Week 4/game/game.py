import random

while True:
    try:
        level = int(input("Level: "))
        n = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
