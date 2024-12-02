from lib.check_codeword import *

def test_check_wrong_codeword():
    codeword = "donkey"
    result = check_codeword(codeword)
    assert result == "WRONG!"

def test_check_close_codeword():
    codeword = "hoarse"
    result = check_codeword(codeword)
    assert result == "Close, but nope."

def test_check_right_codeword():
    codeword = "horse"
    result = check_codeword(codeword)
    assert result == "Correct! Come in."