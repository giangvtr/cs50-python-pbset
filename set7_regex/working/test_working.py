import pytest
from working import convert

def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00" #midnight and noon

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM") #invalid minute
    with pytest.raises(ValueError):
        convert("13:00 PM to 5:00 PM") #invalid hour
    with pytest.raises(ValueError): # invalid format
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")

