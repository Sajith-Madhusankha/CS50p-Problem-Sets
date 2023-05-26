def main():
    text = input("Input: ")
    output = shorten(text)
    print (f"Output: {output}")


def shorten(word):
    short = []
    for i in word:
        if i.lower() not in ["a", "e", "i", "o", "u"]:
            short.append(i)
    shortened = str("".join(short))
    return shortened

print()


if __name__ == "__main__":
    main()