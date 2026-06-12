import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from dictionary import Dictionary
 
 
def test_existing_entry():
    d = Dictionary()
    d.newentry('Apple', 'A fruit that grows on trees')
    assert d.look('Apple') == 'A fruit that grows on trees'
 
def test_missing_entry():
    d = Dictionary()
    assert d.look('Banana') == "Can't find entry for Banana"
 
def test_overwrite_entry():
    d = Dictionary()
    d.newentry('Apple', 'First definition')
    d.newentry('Apple', 'Second definition')
    assert d.look('Apple') == 'Second definition'
 
def test_multiple_entries():
    d = Dictionary()
    d.newentry('Cat', 'A small feline')
    d.newentry('Dog', 'A loyal companion')
    assert d.look('Cat') == 'A small feline'
    assert d.look('Dog') == 'A loyal companion'
 