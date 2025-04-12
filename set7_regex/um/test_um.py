import pytest
from um import count

def test_count():
    assert count("umbrella") == 0
    assert count("Um, hello world, um, um") == 3
    assert count("um...") == 1
