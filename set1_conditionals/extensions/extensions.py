def char_after_dot(input_string):
    # Find the position of the period '.'
    index = input_string.rfind('.')
    return input_string[index + 1:]

def char_filename(input_string):
    index = input_string.rfind('.')
    return input_string[:index]

def main():
    filename = input("File name :").strip().lower()
    if filename.endswith("gif") or filename.endswith("png"):
        print("image/" + char_after_dot(filename))
    elif filename.endswith("jpg") or filename.endswith("jpeg"):
        print("image/" + "jpeg")
    elif filename.endswith("pdf") or filename.endswith("zip") :
        print("application/" + char_after_dot(filename))
    elif filename.endswith("txt") :
        print("text/" + char_filename(filename))

    else:
        print("application/octet-stream")

main()
