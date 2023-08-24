from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2 #solved
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0, 2) == []
    assert arrs.my_slice([1, 2, 3, 4], None, None) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], None, 2) == [1, 2]


