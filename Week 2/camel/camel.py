text = input("camelCase: ")
print("snake_case: ", end="")

for i in text:
    if i.isupper():
        i = i.lower()
        print("_" + i, end="")
    else:
        print(i, end="")
print()