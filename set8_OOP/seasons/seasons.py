import inflect
import sys
from datetime import date
#datetime package is different from date object (that has pre-determined functions)

def main():
    print(demand())

def demand(birth=None):
    if birth is None:
        birth = input('Date of birth: ').strip()
    try:
        birthdate = date.fromisoformat(birth) #return a date object
    except ValueError:
        sys.exit("Invalid date")
    minutes = calcul(birthdate)
    return toString(minutes)

def calcul(birthdate):
    today = date.today()
    deltadate = today - birthdate
    return deltadate.days * 24 * 60

def toString(minutes):
    p = inflect.engine()
    output = p.number_to_words(minutes, andword="").capitalize()
    return output + " minutes"

if __name__ == "__main__":
    main()
