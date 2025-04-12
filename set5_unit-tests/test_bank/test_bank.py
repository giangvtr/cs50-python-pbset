from bank import value

def test_shorten():
    assert value("Hello") == 0
    assert value("Hello, Giang") == 0
    assert value(" How you doing") == 20
    assert value("What's up?") == 100
