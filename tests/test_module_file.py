# test_module_file.py

from my_module.module_file import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-1, 7) == -7

def test_divide():
    assert divide(6, 2) == 3.0
    assert divide(10, 5) == 2.0
    assert divide(0, 5) == 0.0

def test_divide_by_zero():
    try:
        divide(1, 0)
        assert False, "Expected ValueError but didn't get one"
    except ValueError:
        pass
