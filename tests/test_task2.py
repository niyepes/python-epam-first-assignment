import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from task2_how_much import get_total
 
 
costs = {'socks': 5, 'shoes': 60, 'sweater': 30}
 
def test_basic_case():
    assert get_total(costs, ['socks', 'shoes'], 0.09) == 70.85
 
def test_unknown_item_is_ignored():
    assert get_total(costs, ['socks', 'hat'], 0.00) == 5.0
 
def test_empty_items():
    assert get_total(costs, [], 0.09) == 0.0
 
def test_zero_tax():
    assert get_total(costs, ['sweater'], 0.00) == 30.0
 
def test_all_items_unknown():
    assert get_total(costs, ['hat', 'gloves'], 0.10) == 0.0
 
def test_rounding():
    assert get_total({'a': 1}, ['a'], 0.001) == 1.0
