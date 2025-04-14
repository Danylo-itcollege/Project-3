# test_lab.py

from lab import add, subtract

def test_add():
    assert add(4, 7) == 8

def test_subtract():
    assert subtract(3, 7) == 3
