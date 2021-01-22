'''
author: a5892731
date: 2021-01-22

This is test file for fibo module

_________________________

Remember to install:
pip install pytest

------------------
test largest_prime_factor_from_number(number): function
'''

import pytest

from prime_factor import largest_prime_factor_from_number


def input_output_for_test_generator(file_address = "prime_numbers.txt"):
    file = open(file_address, 'r')
    prime_numbers_list = file.split(" ")
    input_number = 2
    input_numbers_list = []
    output_numbers_list = []

    for number in prime_numbers_list:
        print(number)

        while input_number <= number:
            input_numbers_list.append(input_number)
            input_number += 1
            output_numbers_list.append(number)
    file.close()
    return input_numbers_list, output_numbers_list


def largest_prime_factor_from_number(number, expected):

    output = largest_prime_factor_from_number(number)
    print(">>> >>> range {} max prime number: {}".format(number, output))
    assert output == expected



def tests_run():
    input_output = []
    input_output = input_output_for_test_generator()

    for element in input_output[0]:
        largest_prime_factor_from_number(element, input_output[1])





