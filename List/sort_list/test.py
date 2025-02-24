from random import randint
from .solution import sort_list


def test_sorted_list():
    rand_lst = [randint(-2 ** 10, 2 ** 10) for _ in range(15)]
    assert sort_list(rand_lst) == sorted(rand_lst)
