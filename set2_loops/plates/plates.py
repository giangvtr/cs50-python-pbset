import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1st condition: The first 2 characters are letters
    if not s[:1].isalpha():  # corrected slicing to check the first 2 characters
        return False

    # 2nd condition: max 6 characters and min 2 characters
    if not (2 <= len(s) <= 6):
        return False

    # 3rd condition: Numbers cannot be in the middle of the plate
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            if not s[i:].isdigit():  # remaining characters must be all digits
                return False
            if c == '0' and not s[i-1].isdigit():  # no leading zeros unless it follows another digit
                return False
            break # loop break when 1 digit are found and the char following are ok

    # 4th condition: No periods, spaces, or punctuation marks
    for c in s:
        if c in ['.', ' '] or c in string.punctuation:
            return False

    return True
main()
