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

def max_palindromic_num_test(num_1, num_2):
    output_list = [1]
    for num1 in range(num_1, 0, -1):
        for num2 in range(num_2, 0, -1):
            output = num1 * num2
            if str(output) == str(output)[::-1]:
                output_list.append(output)

    return max(output_list)  # check max for all posibilities


@pytest.mark.parametrize("number, number2, expected",[
    (number, number, max_palindromic_num_test(number, number)) for number in range(1, 200)
])


def test_palindromic_num_from_mul_of_two_num(number, number2, expected):

    output = palindromic_num_from_mul_of_two_num(number, number2)
    print(">>> >>> range {} and {} max palindromic number: {} expected {}".format(number,number2, output, expected))
    assert output == expected



@pytest.mark.parametrize("number, number2, expected",[
    (number, number, max_palindromic_num_test(number, number)) for number in range(800, 1000)
])


def test_palindromic_num_from_mul_of_two_num2(number, number2, expected):

    output = palindromic_num_from_mul_of_two_num(number, number2)
    print(">>> >>> range {} and {} max palindromic number: {} expected {}".format(number, number2, output, expected))
    assert output == expected
