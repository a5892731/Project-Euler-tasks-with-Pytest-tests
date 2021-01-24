'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def least_common_multiple_in_list(num_list):
    common_div = min(num_list) # it just cant be less than smallest number on table
    output_list = []
    for number in range(0, len(num_list), 2):
        output_list.append(least_common_multiple(num_list[number -1], num_list[number]))

    #print(output_list)

    if len(output_list) > 1:
        output_list = least_common_multiple_in_list(output_list)
    return output_list

def greatest_common_divisor(num1, num2):  # it can be more optimal, but its fine
    max_divisor = min(num1, num2) # divisor cant be bigger than smallest number
    while True:
        if num1 % max_divisor == 0 and num2 % max_divisor == 0:
            break
        max_divisor -= 1
    return max_divisor

def least_common_multiple(num1, num2):  # it can be more optimal, but its fine
    max_mul = max(num1, num2) # it just cant be less than biggest number on table
    common_div = greatest_common_divisor(num1, num2)

    while True:
        if max_mul % num1 == 0 and max_mul % num2 == 0:
            break
        max_mul += common_div

    return max_mul


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

print(least_common_multiple(9, 12))

print(least_common_multiple_in_list(list(range(1, 14 + 1)))[0]) # if you like to have 20 in list you must add 1
#print(smallest_num_that_can_be_div_by(1, 14))