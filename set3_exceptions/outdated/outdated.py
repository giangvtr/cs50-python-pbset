months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    month, date, year = get_command("Date: ")
    print(f"{year}-{month:02d}-{date:02d}")


def get_command(prompt):
    while True:
        date_string = input(prompt).title().strip()

        # Check if MM/DD/YYYY
        if '/' in date_string:
            parts = date_string.split('/')
            if len(parts) == 3:
                try:
                    month = int(parts[0])
                    if month > 12:
                        raise ValueError
                    date = int(parts[1])
                    if date > 31:
                        raise ValueError
                    year = int(parts[2])
                    return month, date, year
                except ValueError:
                    pass

        # Check if Month DD, YYYY
        for m in months:
            if date_string.startswith(m) and ',' in date_string:
                try:
                    rest = date_string[len(m):].strip()
                    date, year = rest.split(',')
                    date = int(date.strip())
                    if date > 31:
                        raise ValueError
                    year = int(year.strip())
                    month = months.index(m) + 1  # Fix: use m instead of m+1, add 1 to index
                    return month, date, year
                except ValueError:
                    pass

if __name__ == "__main__":
    main()
