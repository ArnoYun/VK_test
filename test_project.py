import pytest as pytest

tuple_sample = ('sample', 1, [6, 7, 8], 'ok', 99, 'number', 99)

# def test_index():
#     with pytest.raises(ValueError):
#         tuple_sample.index(100)
def test_index():
    assert tuple_sample.index([6, 7, 8]) == 2

def test_count():
    assert  tuple_sample.count(99) == 2

def test_position():
    try: assert tuple_sample[7]
    except: IndexError








