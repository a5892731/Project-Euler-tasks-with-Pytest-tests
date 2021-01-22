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


def output_for_test_generator(input_number, file_address = "prime_numbers.txt"):
    file = open(file_address, 'r')

    prime_numbers_list = [int(line) for line in file]
    print(">>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>> >>>")
    print(">>>>>>>>>>>>>>> >>>>>>>>>>>>>>>>>>>>> >>>" + str(prime_numbers_list))
    file.close()

    output = 1
    for prime_number in prime_numbers_list:
        print(str(input_number) + str(prime_number))
        print(prime_number)
        if input_number < prime_number:
            output = prime_number
        if prime_number >= input_number:
            break

    return output


@pytest.mark.parametrize("number, expected",[
    (7, output_for_test_generator(7)),

])


def test_largest_prime_factor_from_number(number, expected):



    output = largest_prime_factor_from_number(number)

    print(">>> >>> range {} max prime number: {}".format(number, output))
    assert output == expected






