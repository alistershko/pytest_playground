from lib.string_builder import *

def test_no_input():
    test_str = ""
    no_input = StringBuilder()
    no_input.add(test_str)
    size = no_input.size()
    result = no_input.output()
    assert size == 0
    assert result == ""

def test_add_one_string():
    test_str_01 = "Hello"
    one_string = StringBuilder()
    one_string.add(test_str_01)
    size = one_string.size()
    result = one_string.output()
    assert size == 5
    assert result == "Hello"

def test_add_two_strings():
    test_str_01 = "Hello"
    test_str_02 = " world!"
    two_string = StringBuilder()
    two_string.add(test_str_01)
    two_string.add(test_str_02)
    size = two_string.size()
    result = two_string.output()
    assert size == 12
    assert result == "Hello world!"