from series import fibonacci, lucas, sum_series

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(7) == 13


def test_lucas():
    assert lucas(-1) == print("Please input a positive integer")
    assert lucas(0) == 2
    assert lucas(7) == 29


def test_sum_series():
    assert sum_series(7) == 13
    assert sum_series(7, 2, 1) == 29
    assert sum_series(7, 5, 4) == 92

