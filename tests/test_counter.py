from lib.counter import *

def test_no_change():
    no_change = Counter()
    no_change.add(0)
    result = no_change.report()
    assert result == "Counted to 0 so far."

def test_count_to_two():
    two_count = Counter()
    two_count.add(2)
    result = two_count.report()
    assert result == "Counted to 2 so far."

def test_count_to_big_number():
    big_count = Counter()
    big_count.add(12034982134002319412)
    result = big_count.report()
    assert result == "Counted to 12034982134002319412 so far."

def test_count_two_then_three():
    two_three = Counter()
    two_three.add(2)
    two_three.add(3)
    result = two_three.report()
    assert result == "Counted to 5 so far."