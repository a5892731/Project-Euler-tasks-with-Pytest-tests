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
    if len == 0:
        return [0]
    if len == 1:
        return [0, actual_fibo_num]
    if len > 1:
        for num in range(1, len):
            output = actual_fibo_num + last_fibo_num
            last_fibo_num = actual_fibo_num
            actual_fibo_num = output
        return actual_fibo_num


def fibonacci_initialization():
    fibonacci = Fibonacci()
    assert fibonacci

@pytest.mark.parametrize("fibo len, expected",[
    (1, fibo_gen(1)),
    (2, fibo_gen(2)),
    (3, fibo_gen(3)),
    (4, fibo_gen(4)),
    (5, fibo_gen(5)),
    (10, fibo_gen(10)),
    (20, fibo_gen(20)),
    (30, fibo_gen(30)),
    (40, fibo_gen(40)),
    (50, fibo_gen(50)),
])


def test_fibonnaci_sequece_generator(length_of_fibonnaci_sequece, expected):
    fibonacci = Fibonacci()
    fibonacci.secuence_len = length_of_fibonnaci_sequece
    fibonacci.__init__()
    print(">>> >>>RANGE {} FIBONACCI LIST: {}".format(fibonacci.secuence_len, fibonacci.fibo_list))
    assert fibonacci.fibo_list == expected


@pytest.mark.parametrize("fibo len, expected",[
    (1, 1),
    (2, 2),
    (3, 4),
    (4, 7),
    (5, 12),
    (10, 143),
    (20, 17710),
    (30, 2178308),
    (40, 267914295),
    (50, 20365011073),
])

def test_fibonnaci_sequece_sum(length_of_fibonnaci_sequece, expected):
    fibonacci = Fibonacci()
    fibonacci.secuence_len = length_of_fibonnaci_sequece
    fibonacci.__init__()
    print(">>> >>>RANGE {} FIBONACCI LIST: {}".format(fibonacci.secuence_len, fibonacci.sum_of_fibo_num))
    assert fibonacci.sum_of_fibo_num == expected


