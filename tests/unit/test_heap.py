from pbz.dtypes.heap import *

def test_creation():
    h = MinHeap([4, 5, 2, 1, 9, 10])
    assert h.pop() == 1
    assert h.pop() == 2
    assert h.pop() == 4

    h = MaxHeap([4, 5, 2, 1, 9, 10])
    assert h.pop() == 10
    assert h.pop() == 9
    assert h.pop() == 5

def test___repr__():
    pass

def test_assignment():
    pass

def test___iter__():
    pass



def test_comparison_operators():
    pass
