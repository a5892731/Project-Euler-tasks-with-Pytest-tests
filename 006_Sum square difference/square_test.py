'''
author: a5892731
date: 2021-01-25

This is test file for fibo module

_________________________

Remember to install:
pip install pytest

------------------

'''
import pytest

from square import sum_of_the_squares, square_of_the_sum

@pytest.mark.parametrize("input_list, expected",[
    ([2], 4),
    (list(range(1, 101)), 338350),
    ([num*2 for num in range(1, 101)], 1353400)

])

def test_sum_of_the_squares(input_list, expected):

    output = sum_of_the_squares(input_list)
    print(">>> >>> in1 {} out: {} expected {}".format(input_list, output, expected))
    assert output == expected


@pytest.mark.parametrize("input_list, expected", [
    ([2], 4),
    (list(range(1,101)), 25502500),
    ([num*2 for num in range(1, 101)], 102010000)

])
def test_square_of_the_sum(input_list, expected):
    output = square_of_the_sum(input_list)
    print(">>> >>> in1 {} out: {} expected {}".format(input_list, output, expected))
    assert output == expected


