from solutions.sum_list import sum_list

def test_sum_list_basic():
    assert sum_list([1, 2, 3]) == 6

def test_sum_list_empty():
    assert sum_list([]) == 0
