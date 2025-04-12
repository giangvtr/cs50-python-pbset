# Get the input from the user
user_input = input('camelCase: ').strip()

# Initialize an empty list to store the output characters
output = []

# Iterate over each character in the input string
for c in user_input:
    if not c.isupper():
        # If the character is not uppercase, append it to the output list
        output.append(c)
    else:
        # If the character is uppercase, append an underscore and the lowercase version of the character
        output.append('_')
        output.append(c.lower())

# Join the list into a single string and print it
print(f"snakecase: {''.join(output)}")
