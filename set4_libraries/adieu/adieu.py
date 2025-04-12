def main():
    name_list = get_command()
    print("\n")
    if len(name_list) == 1:
        print(f"Adieu, adieu, to {name_list[0]}")
    elif len(name_list) == 2:
        print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")
    else:
        print(f"Adieu, adieu, to {', '.join(name_list[:-1])}, and {name_list[-1]}")

def get_command():
    name_list = []
    print("Enter names (Ctrl+D to finish):")
    while True:
        try:
            user_input = input("Name: ").strip().title()
            if user_input and user_input not in name_list:
                name_list.append(user_input)
        except EOFError:
            print()  # Print a newline character for a cleaner exit
            break
    return name_list

if __name__ == "__main__":
    main()

