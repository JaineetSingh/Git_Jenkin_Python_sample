# tests/test_app.py

from main import add

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed_numbers():
    assert add(5, -3) == 2

def test_add_mixed_numbers2():
    assert add(5, -3) == 22