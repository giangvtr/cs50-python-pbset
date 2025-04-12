from numb3rs import validate

def test_validate():
    assert validate("255.255.34.0") == True
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True

    assert validate("256.100.100.100") == False  # First octet out of range
    assert validate("100.256.100.100") == False  # Second octet out of range
    assert validate("100.100.256.100") == False  # Third octet out of range
    assert validate("100.100.100.256") == False  # Fourth octet out of range
    assert validate("1.2.3.4.5") == False        # Too many octets
    assert validate("1.2.3") == False            # Too few octets
    assert validate("1.2.3.") == False           # Trailing dot
    assert validate(".1.2.3.4") == False         # Leading dot
    assert validate("1.2.3.4a") == False         # Extra characters at the end
    assert validate("1234.1.1.1") == False       # First octet too long
    assert validate("1.1234.1.1") == False       # Second octet too long
    assert validate("1.1.1234.1") == False       # Third octet too long
    assert validate("1.1.1.1234") == False       # Fourth octet too long
