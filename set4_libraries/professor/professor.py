import random

def main():
    level = get_level()
    score = 0
    print("\n")
    for _ in range(10):
        X, Y = generate_integer(level)
        target = X + Y
        print(f"{X} + {Y} = ", end="")

        for tries in range(3) :
            try :
                user_guess = int(input())
                if user_guess  == target :
                    score += 1
                    break
                elif user_guess < 1:
                    raise ValueError
                else:
                    print("EEEE")
            except ValueError:
                print('EEEE')

        if user_guess != target :
            print(f"{X} + {Y} = {target}")
    print(f"Score : {score}")

def get_level():
    while True :
        try:
            level = int(input("Level: ").strip())
            if level in [1, 2, 3]:
                return level
            else :
                raise ValueError
        except ValueError:
            continue

def generate_integer(level) :
        if level == 1:
            X = random.randint(0,10)
            Y = random.randint(0,10)
        elif level == 2:
            X= random.randint(10,99)
            Y = random.randint(10,99)
        elif level == 3:
            X = random.randint(100,999)
            Y = random.randint(100,999)
        return X, Y

if __name__ == "__main__":
    main()

