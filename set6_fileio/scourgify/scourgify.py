import sys
import csv

def valid_arg(args):
    if len(args) < 3:
        print("Too few command-line argument")
        sys.exit(1)
    elif len(args) > 3:
        print("Too many command-line argument")
        sys.exit(1)
    elif not args[1].endswith('.csv'):
        print("Not a CSV file")
        sys.exit(1)
    return args[1], args[2] #return the file name

def open_file(filename):
    try :
        with open(filename, 'r') as file:
            reader = csv.DictReader(file) #Create multiple dictionaries
            data = list(reader) # Put those dictionaries into a list
        return data
    except FileNotFoundError:
        print(f"Could not read {filename}")
        sys.exit(1)

def write_file(filename, data):
    with open(filename, 'w', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = ['first', 'last', 'house'])  # initialise the new csv file
        writer. writeheader() #write in header in the new file
        for row in data:
            last, first = row["name"].strip('"').split(', ')
            writer.writerow({"first": first, "last": last, "house": row["house"]})

def main():
    input_file, output_file = valid_arg(sys.argv)
    data = open_file(input_file)
    write_file(output_file, data)


if __name__== "__main__":
    main()
