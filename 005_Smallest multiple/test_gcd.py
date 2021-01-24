'''
author: a5892731
date: 2021-01-24

This is test file for fibo module

_________________________

Remember to install:
pip install pytest

------------------
test greatest_common_divisor functions

'''



import pytest

from gcd import greatest_common_divisor


def smallest_num_that_can_be_div_by(min_range = 1, max_range = 10): # its working but not optimal
    output = 0
    number = 1
    while True:
        div_counter = 0
        for divisor in range(min_range, max_range + 1):
            if number % divisor == 0:
                div_counter += 1
            if div_counter == (max_range - min_range + 1):
                output = number
                break
        if output > 0:
            break
        number += 1
    return output




@pytest.mark.parametrize("number, number2, expected",[
    (9, 6, 18),
    (12, 6, 12),
    (12, 48, 48),
    (51, 48, 816),
    (51, 481, 24531),
    (223, 481, 107263),
    (223, 1481, 330263),
])

def greatest_common_divisor_test(number, number2, expected):

    output = greatest_common_divisor(number, number2)
    print(">>> >>> in1 {} in2 {} out: {} expected {}".format(number, number2, output, expected))
    assert output == expected

