'''
author: a5892731
date: 2021-01-22

This is test file for fibo module

_________________________

Remember to install:
pip install pytest

------------------
test palindromic_num_from_mul_of_two_num(num_1 = 999, num_2 = 999): function
'''


import pytest

from palindrome import palindromic_num_from_mul_of_two_num

def test_palindromic_num_from_mul_of_two_num(num_1 = 999, num_2 = 999):
    output_list = []
    for num1 in range(num_1, 0, -1):
        for num2 in range(num_2, 0, -1):
            output = num1 * num2
            if str(output) == str(output)[::-1]:
                output_list.append(output)

    return max(output_list)


@pytest.mark.parametrize("number, expected",[
    (number, test_palindromic_num_from_mul_of_two_num(number)) for number in range(1, 1000)
])


def test_largest_prime_factor_from_number(number, expected):

    output = largest_prime_factor_from_number(number)
    print(">>> >>> range {} max prime number: {}".format(number, output))
    assert output == expected

