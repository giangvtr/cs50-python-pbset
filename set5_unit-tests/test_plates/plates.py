import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1st condition: The first 2 characters are letters
    if len(s) < 2 or not s[:2].isalpha():
        print("Failing at first condition")
        return False

    # 2nd condition: max 6 characters and min 2 characters
    if not (2 <= len(s) <= 6):
        print("Failing at length condition")
        return False

    # 3rd condition: Numbers cannot be in the middle of the plate
    for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                if not s[i:].isdigit():
                    print("Failing at number placement condition")
                    return False
                if c == '0' and not s[i-1].isdigit():
                    print("Failing at zero condition")
                    return False
                break

    # 4th condition: No periods, spaces, or punctuation marks
    for c in s:
        if c in ['.', ' '] or c in string.punctuation:
            print("Failing at punctuation condition")
            return False

    return True

if __name__ == "__main__":
    main()
