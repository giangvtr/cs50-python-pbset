def main():
    clock = input("What time is it? ").strip()
    clock = convert(clock)
    if 7.0 <= clock <= 8.0:
        print("breakfast time")
    elif 12.0 <= clock <= 13.0:
        print("lunch time")
    elif 18.0 <= clock <= 19.0:
        print("dinner time")


def convert(time):
    # convert time to float for ex 7:30 is 7,5
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return float( hours + minutes/60)


if __name__ == "__main__":
    main()
