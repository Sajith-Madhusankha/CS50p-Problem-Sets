text = input("Input: ")
print("Output: ", end="")

for i in text:
    if i.lower() in ["a", "e", "i", "o", "u"]:
        i = i.replace(i, "")
        print(i, end="")
    else:
        print(i, end="")
print()