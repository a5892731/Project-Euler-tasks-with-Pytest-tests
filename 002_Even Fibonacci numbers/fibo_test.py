'''
author: a5892731
date: 2021-01-21

This is test file for fibo module

_________________________

Remember to install:

pip install pytest

------------------

fibonaci numbers
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...


https://www.mathsisfun.com/numbers/fibonacci-sequence.html


'''

import pytest

from fibo import Fibonacci

def fibo_gen(len):
    last_fibo_num = 1
    actual_fibo_num = 1
    fibo_list = [0, 1]
    if len == 0:
        return [0]
    if len == 1:
        return fibo_list
    if len > 1:
        for num in range(1, len):
            output = actual_fibo_num + last_fibo_num
            last_fibo_num = actual_fibo_num
            actual_fibo_num = output
            fibo_list.append(last_fibo_num)

        return fibo_list


def fibonacci_initialization():
    fibonacci = Fibonacci()
    assert fibonacci

@pytest.mark.parametrize("length_of_fibonnaci_sequece, expected",[
    (0, [0]),
    (1, fibo_gen(1)),
    (10, fibo_gen(10)),
    (15, fibo_gen(15)),
    (20, fibo_gen(20)),
    (32, fibo_gen(32)),
    (41, fibo_gen(41))
])


def test_fibonnaci_sequece_generator(length_of_fibonnaci_sequece, expected):
    fibonacci = Fibonacci()
    fibonacci.secuence_len = length_of_fibonnaci_sequece
    fibonacci.fibonnacci_sequece_generator()

    print(">>> >>>RANGE {} FIBONACCI LIST SUM: {}".format(fibonacci.secuence_len, fibonacci.fibo_list))
    assert fibonacci.fibo_list == expected


@pytest.mark.parametrize("length_of_fibonnaci_sequece, expected",[
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7),
    (5, 12),
    (10, 143),
    (20, 17710),
    (30, 2178308),
    (40, 267914295),
])

def test_fibonnaci_sequece_sum(length_of_fibonnaci_sequece, expected):
    fibonacci = Fibonacci()
    fibonacci.secuence_len = length_of_fibonnaci_sequece
    fibonacci.fibonnacci_sequece_generator()
    fibonacci.fibonacci_list_sum()
    print(">>> >>>RANGE {} FIBONACCI LIST SUM: {}".format(fibonacci.secuence_len, fibonacci.sum_of_fibo_num))
    assert fibonacci.sum_of_fibo_num == expected


def test_fibonaci_max_num_list(expected = 3524578): # for default max value that is les than 4 000 000
    fibonacci = Fibonacci()
    fibonacci.fibonaci_list_up_to_num()
    fibonacci.fibonacci_list_sum()
    print(">>> >>>max number {} FIBONACCI LIST: {}".format(fibonacci.max_value, fibonacci.fibo_list))
    print(">>> >>>FIBONACCI LIST SUM: {}".format(fibonacci.sum_of_fibo_num))
    assert fibonacci.fibo_list[-1] == expected




