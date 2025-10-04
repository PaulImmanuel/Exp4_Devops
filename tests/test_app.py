from app import add

def test_app():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_simple():
    assert add(1, 1) == 2
