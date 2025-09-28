import os.path
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.calculator import add

def test_add():
    assert add("1,2") == 3
