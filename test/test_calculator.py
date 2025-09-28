import os.path
import sys
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from src.calculator import add

def test_add_no_digit():
    assert add("") == 0

def test_add():
    assert add("1,2") == 3

def test_add_new_line():
    assert add("1\n2,3") == 6

def test_add_new_delimiter():
    assert add("//;\n1;2") == 3

def test_add_negatives():
    with pytest.raises(ValueError, match="negative numbers not allowed -1000,-2"):
        add("//;\n-1000;-2")
