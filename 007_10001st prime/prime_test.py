'''
author: a5892731
date: 2021-01-25

This is test file for fibo module

_________________________

Remember to install:
pip install pytest

test data from https://en.wikipedia.org/wiki/List_of_prime_numbers and https://primes.utm.edu/lists/small/10000.txt

------------------

'''
import pytest

from prime import prime_num



@pytest.mark.parametrize("input, expected",[
    (0, None),
    (1, 2),
    (2, 3),
    (3, 5),
    (4, 7),
    (5, 11),
    (6, 13),
    (6, 13),
    (20, 71),
    (221, 1381),
    (401, 2749),
    (841, 6481),
    (1000, 7919),
    (10000, 104729)
])

def test_prime_num(input, expected):

    output = prime_num(input)
    print(">>> >>> in1 {} out: {} expected {}".format(input, output, expected))
    assert output == expected