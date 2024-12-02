import pytest
from lib.password_checker import *

def test_valid():
    valid = PasswordChecker()
    password = "eightormorecharacters"
    result = valid.check(password)
    assert result == True

def test_invalid():
    invalid = PasswordChecker()
    password = "invalid"
    with pytest.raises(Exception) as e:
        invalid.check(password)
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."