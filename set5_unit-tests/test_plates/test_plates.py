from plates import is_valid

def test_first2letters():
    assert is_valid("ETC108") == True
    assert is_valid("8AAJOF") == False
    assert is_valid("A8AJOF") == False  # Added this test case
    assert is_valid("EW94") == True
    assert is_valid("50") == False

def test_length():
    assert is_valid("SLDKJ") == True
    assert is_valid("3") == False
    assert is_valid("JSIDJW4") == False

def test_nbmiddle():
    assert is_valid('AAA222') == True   # Changed this test case
    assert is_valid('AAA22A') == False  # Changed this test case
    assert is_valid("ETC008") == False # no leading zero

def test_punc():
    assert is_valid("JF.UI") == False
    assert is_valid("SDK JS1") == False
