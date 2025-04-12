menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    get_command("Item: ")

def get_command(prompt):
    total = 0
    while True:
        try:
            item = input(prompt).title().strip()
        except EOFError:
            return total
        try:
            total += float(menu[item])
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass


if __name__ == "__main__":
    main()
