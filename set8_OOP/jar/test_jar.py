from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar("-1") #invalid capacity


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    assert jar1.deposit(3) == 3
    jar2 = Jar()
    with pytest.raises(ValueError):
        jar2.deposit(13)

def test_withdraw():
    jar1 = Jar()
    jar1.deposit(2)
    assert jar1.withdraw(1) == 1
    jar2 = Jar()
    with pytest.raises(ValueError):
        jar2.withdraw(2)
