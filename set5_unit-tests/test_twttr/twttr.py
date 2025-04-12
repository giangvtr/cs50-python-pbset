def main():
    user_input = input("Input: ").strip()
    output = shorten(user_input)
    print(f"Output: {output}")

def shorten(word):
    output = ""
    for c in word:
        if not c in ['A', 'a', 'u', 'U', 'i', 'I', 'o', 'O', 'e', 'E']:
            output += c
        else:
            continue
    return output

if __name__ == "__main__":
    main()


