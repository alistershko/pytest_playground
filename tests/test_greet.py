from lib.greet import *

def test_greet():
    result = greet("Alister")
    assert result == "Hello, Alister"