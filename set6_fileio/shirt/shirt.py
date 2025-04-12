import sys
from os.path import splitext
from PIL import Image, ImageOps

def is_valid_image_extension(filename):
    return filename.lower().endswith(('.jpg', '.jpeg', '.png'))

def valid_arg(args):
    if len(args) != 3:
        sys.exit("Incorrect number of command-line arguments")

    if not (is_valid_image_extension(args[1]) and is_valid_image_extension(args[2])):
        sys.exit("Invalid input")

    return args[1], args[2]  # Return the file names

def coherent_files(file1, file2):
    _, file_ext1 = splitext(file1)
    _, file_ext2 = splitext(file2)
    if file_ext1 != file_ext2:
        sys.exit("Input and output have different extensions")
    return file_ext2[1:]   # Return the file extension without the dot

# Open the shirt image
def open_file(file):
    try :
        return Image.open(file)

    except FileNotFoundError:
        sys.exit(f"Could not read {file}")

# Pasting
def paste(shirt, input_image):
    input_image = ImageOps.fit(input_image, shirt.size)
    result = input_image.copy()
    result.paste(shirt, shirt)
    return result


def main():
    input_file, output_file = valid_arg(sys.argv)
    file_ext = coherent_files(input_file, output_file)

    shirt = open_file("shirt.png")
    input_image = open_file(input_file)

    output_image = paste(shirt, input_image)
    output_image.save(output_file)

if __name__ == "__main__":
    main()

