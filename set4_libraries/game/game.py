import random

def main():
    level = get_command()
    print("\n")
    guess(level)

def get_command():
    name_list = []
    print("Enter level (Ctrl+D to finish):")
    while True :
        try:
            level = int(input("Level: ").strip())
            if level < 1:
                raise ValueError
            else :
                return random.randint(1, level)
        except ValueError:
            continue

def guess(level) :
    while True :
        try :
            user_guess = int(input("Guess: "))
            if user_guess  == level :
                print('Just right!')
                break
            elif user_guess < 1:
                raise ValueError
            elif user_guess < level:
                print('Too small!')
                continue
            elif user_guess > level :
                print('Too large!')
                continue
        except ValueError:
            print('Please enter a valid integer')


if __name__ == "__main__":
    main()

