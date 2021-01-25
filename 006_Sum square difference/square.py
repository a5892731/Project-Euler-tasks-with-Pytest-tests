'''
The sum of the squares of the first ten natural numbers is, XXXXX

The square of the sum of the first ten natural numbers is, XXXXX

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''


def sum_of_the_squares(list_of_args, power = 2):
    output = 0
    for arg in list_of_args:
        output = output + pow(arg, power)
    return output

def square_of_the_sum(list_of_args, power = 2):
    output = 0
    for arg in list_of_args:
        output = output + arg
    return pow(output, power)


#-------------------------------------------------------------------------------------------------------------------
a = sum_of_the_squares(list(range(1, 100)))
b = square_of_the_sum(list(range(1, 100)))

print(a)
print(b)
print(str(abs(a - b)))