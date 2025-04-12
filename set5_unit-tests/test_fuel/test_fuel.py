from fuel import gauge, convert
import pytest

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    assert gauge(67) == "67%"

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/4") == 50
    assert convert("1/3") == 33
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1/")
    with pytest.raises(ValueError):
        convert("/2")
    with pytest.raises(ValueError):
        convert("10/3")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("4-5")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
