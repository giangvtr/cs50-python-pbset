grocery_list = {}

def main():
    get_command()
    print("\n")
    for item in sorted(grocery_list.keys()):
        print(f"{grocery_list[item]} {item.upper()}")

def get_command():
    while True:
        try:
            item = input().strip()
            if item:  # Check if input is not empty, avoid problem Item: multiple times
                if item not in grocery_list:
                    grocery_list[item] = 1
                else:
                    grocery_list[item] += 1
        except EOFError:
            return grocery_list  # Exit the loop after EOF

    # Sort keys and print results

if __name__ == "__main__":
    main()
