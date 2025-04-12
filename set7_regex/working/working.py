import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r'^(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)$'
    matches = re.search(pattern, s)

    if not matches:
        raise ValueError("Invalid input format")

    start_hour, start_min, start_period, end_hour, end_min, end_period = matches.groups()

    start_time = convert_time(start_hour, start_min, start_period)
    end_time = convert_time(end_hour, end_min, end_period)

    return f"{start_time} to {end_time}"

def convert_time(hour, min, period):
    hour = int(hour) #normal case

    if period == "PM" and hour != 12: #in the afternoon
        hour += 12
    elif period == "AM" and hour == 12: #12AM is midnight
        hour = 0

    if min is None :
        min = "00"

    return f"{hour:02d}:{min}" #hour with a leading 0 ex 09:00

if __name__ == "__main__":
    main()
