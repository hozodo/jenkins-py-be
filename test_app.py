import app

# pytest

def test_func01():
    assert app.func01() == "Hello Jenkins!"

def test_func02():
    assert app.func02() == "Hello Hudson!"