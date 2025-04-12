user_input = input("Input: ").strip()
output = []

for c in user_input:
    if not c in ['A', 'a', 'u', 'U', 'i', 'I', 'o', 'O', 'e', 'E']:
        output.append(c)
    else:
        continue

print(f"Output: {''.join(output)}")
