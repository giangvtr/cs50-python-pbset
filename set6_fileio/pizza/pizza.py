import sys
from tabulate import tabulate
import csv

def valid_arg(args):
    if len(args) < 2:
        print("Too few command-line argument")
        sys.exit(1)
    elif len(args) > 2:
        print("Too many command-line argument")
        sys.exit(1)
    elif not args[1].endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)
    return args[1] #return the file name

def open_file(filename):
    try :
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

def format_csv(data):
    headers = data[0]
    rows = data[1:]
    return tabulate(rows, headers=headers, tablefmt="grid")

def main():
    filename = valid_arg(sys.argv) #got the file name
    csv_data = open_file(filename)
    output = format_csv(csv_data)
    print(output)

if __name__== "__main__":
    main()



