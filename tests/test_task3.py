import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from task3_nth_letter import nth_char
 
 
def test_example_case():
    assert nth_char(["yoda", "best", "has"]) == "yes"
 
def test_empty_list():
    assert nth_char([]) == ""
 
def test_single_word():
    assert nth_char(["hello"]) == "h"
 
def test_longer_list():
    assert nth_char(["abc", "bcd", "cde"]) == "ace"
