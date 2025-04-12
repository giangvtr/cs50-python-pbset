from emoji import emojize

def main():
    # Prompt the user for input
    user_input = input("Input: ")

    # Emojize the input
    emojized_output = emojize(user_input, language='alias')

    # Print the result
    print("Output:", emojized_output)

if __name__ == "__main__":
    main()
