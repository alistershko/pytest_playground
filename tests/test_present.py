import pytest
from lib.present import *

def test_nothing_to_wrap():
    gift = None
    test_no_gift = Present()
    test_no_gift.wrap(gift)
    # result = test_none_gift.unwrap(gift)
    # assert result == "No contents have been wrapped"
    with pytest.raises(Exception) as e:
        test_no_gift.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_already_wrapped():
    gift = "a toy"
    test_toy = Present()
    test_toy.wrap(gift)
    with pytest.raises(Exception) as e:
        test_toy.wrap(gift)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_wrap_and_unwrap():
    gift = "train set"
    test_train_set = Present()
    test_train_set.wrap(gift)
    result = test_train_set.unwrap()
    assert result == "train set"
