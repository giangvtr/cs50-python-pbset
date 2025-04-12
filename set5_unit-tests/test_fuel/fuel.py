def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        result = x / y
        return round(result * 100)
    except ValueError:
        raise
    except ZeroDivisionError:
        raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


if __name__ == "__main__":
    main()
