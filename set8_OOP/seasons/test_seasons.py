from seasons import demand, toString, calcul
from datetime import date

def test_main():
    assert demand("1999-01-01") == "Thirteen million, four hundred fifty-eight thousand, two hundred forty minutes"

def test_toString():
    assert toString(13458240) == "Thirteen million, four hundred fifty-eight thousand, two hundred forty minutes"

def test_calcul():
    assert calcul(date(2023, 8, 3)) == 527040

