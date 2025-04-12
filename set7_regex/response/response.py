import validators

def main():
    print(validate(input("What is your email adress? ")))


def validate(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
