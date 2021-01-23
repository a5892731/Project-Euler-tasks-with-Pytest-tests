'''

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def palindromic_num_from_mul_of_two_num(num_1 = 999, num_2 = 999):

    for num1 in range(num_1, 0, -1):
        for num2 in range(num_2, 0, -1):
            output = num1 * num2
            if str(output) == str(output)[::-1]:
                output

    return output



print(palindromic_num_from_mul_of_two_num())