def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dollars_str = d[1:]
    return float(dollars_str)


def percent_to_float(p):
    percent_str = p[:-1]
    return float(percent_str)/100

main()
