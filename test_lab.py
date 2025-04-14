from lab import add, subtract

def test_add():
    assert add(4, 7) == 11  # Changed from 8 to 11 (correct math)

def test_subtract():
    assert subtract(3, 7) == -4  # Changed from 3 to -4 (correct math)
