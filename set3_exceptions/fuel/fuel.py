def get_fraction(prompt):
    while True:
        fraction = input(prompt)
        try:
            x, y = fraction.split('/')
            x = int(x)
            y = int(y)
            if x>y:
                raise ValueError
            return (x / y) * 100
        except (ValueError, ZeroDivisionError):
            pass

def main():
    fraction = get_fraction("Fraction: ")
    if fraction <= 1:
        print("E")
    elif fraction >= 99:
        print("F")
    else:
        print(f"{fraction:.0f}%")

if __name__ == "__main__":
    main()
