price = 50

while price > 0:
    print(f"Amount Due: {price}" )
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        price -=coin
change_owed = abs(price)
print(f"Change Owed: {change_owed}")