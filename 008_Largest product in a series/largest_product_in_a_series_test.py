'''
author: a5892731
date: 2021-01-26

This is test file for fibo module

_________________________

Remember to install:
pip install pytest



------------------
@pytest.mark.parametrize("input, expected",[

'''
import pytest

from largest_product_in_a_series import find_the_greatest_sequence_of_multiplications, get_data_from_file



def multiple_elements_from_string(input_string):
    output = 1
    for element in input_string:
        output *= int(element)
    return output


@pytest.mark.parametrize("number_of_elements, expected",[
    (4, ['9989', 5832]),

])

def test_find_the_greatest_sequence_of_multiplications(number_of_elements, expected):

    function_output = find_the_greatest_sequence_of_multiplications(get_data_from_file("largest_product_in_a_series.txt"), number_of_elements)


    assert function_output == expected and function_output[1] == multiple_elements_from_string(function_output[0])
