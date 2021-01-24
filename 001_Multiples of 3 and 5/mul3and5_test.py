'''
author: a5892731
date: 2021-01-30

This is test file for mul3and5 module

_________________________

Remember to install:

pip install pytest



'''

import pytest

from mul3and5 import Multiples_3_and_5


def multiples_3_and_5_initialization():
    multiples_3_and_5 = Multiples_3_and_5()
    assert multiples_3_and_5


@pytest.mark.parametrize("div_range, expected",[
    (4, [3]),
    (6, [3, 5]),
    (10, [3, 5, 6, 9]),
    (11, [3, 5, 6, 9, 10]),
])

def test_find_dividers_of_3_or_5(div_range, expected):
    multiples_3_and_5 = Multiples_3_and_5()
    multiples_3_and_5.div_range = div_range
    multiples_3_and_5.find_dividers_of_3_or_5()
    print(">>> >>>RANGE {} DIVIDERSERS LIST: {}".format(div_range, multiples_3_and_5.dividers))
    assert multiples_3_and_5.dividers == expected


@pytest.mark.parametrize("div_range, expected",[
    (4, 3),
    (6, 8),
    (10, 23),
    (11, 33),
])
def test_sum_of_dividers(div_range, expected):
    multiples_3_and_5 = Multiples_3_and_5()
    multiples_3_and_5.div_range = div_range
    multiples_3_and_5.find_dividers_of_3_or_5()
    multiples_3_and_5.find_sum_of_dividers()
    print(">>> >>>RANGE {} DIVIDERSERS SUM: {}".format(div_range, multiples_3_and_5.sum_of_dividers))
    assert multiples_3_and_5.sum_of_dividers == expected

def test_main_class_in_default_range(expected = 233168):
    multiples_3_and_5 = Multiples_3_and_5()
    multiples_3_and_5.find_dividers_of_3_or_5()
    multiples_3_and_5.find_sum_of_dividers()
    print(">>> >>>RANGE {} DIVIDERSERS SUM: {}".format(1000, multiples_3_and_5.sum_of_dividers))
    assert multiples_3_and_5.sum_of_dividers == expected