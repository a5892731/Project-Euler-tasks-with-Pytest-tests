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
    (3, [3]),
    (5, [3, 5]),
    (10, [42])])

def test_find_dividers_of_3_or_5(div_range, expected):
    multiples_3_and_5 = Multiples_3_and_5()
    multiples_3_and_5.div_range = div_range
    multiples_3_and_5.__init__()
    print(">>> >>>RANGE {} DIVIDERS LIST: {}".format(div_range, multiples_3_and_5.dividers))
    assert multiples_3_and_5.dividers == expected
