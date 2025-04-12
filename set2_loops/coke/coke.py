coin_total = 0

while coin_total < 50:
    print(f"Amount Due: {50 - coin_total}")
    coin_insert = int(input("Insert coin: "))
    if coin_insert in [25, 10, 5]:
        coin_total += coin_insert
    else:
        continue

if coin_total >= 50:
    print(f"Change Owed: {coin_total - 50}")

