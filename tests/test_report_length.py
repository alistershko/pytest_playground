from lib.report_length import *

def test_report_length_zero():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_report_length_five():
    result = report_length("five!")
    assert result == "This string was 5 characters long."

def test_report_length_twentysix():
    result = report_length("abcdefghijklmnopqrstuvwxyz")
    assert result == "This string was 26 characters long."