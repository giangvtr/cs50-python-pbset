import sys
import requests

def valid_arg(args):
    if len(args) < 2:
        print("Too few command-line argument")
        sys.exit(1)
    elif len(args) > 2:
        print("Too many command-line argument")
        sys.exit(1)
    elif not args.endswith('.py'):
        print("Not a Python file")
        sys.exit(1)
    return True

def open_file(filename):
    try :
        with open(sys.argv[1], 'r') as file:
            return file.readlines() #est une liste
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def count_lines(list_lines):
    count = 0
    for line in list_lines:
        line = line.lstrip() #remove leading blanks
        if line != "" and not line.startswith("# "): #check it is not a blank line or a comment line
            count += 1
    return count

def main():
    if valid_arg(sys.argv):
        lines = open_file(sys.argv[1])
        line_count = count_lines(lines)
        print(line_count)

if __name__== "__main__":
    main()
