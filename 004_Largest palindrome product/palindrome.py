'''

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def palindromic_num_from_mul_of_two_num(num_1 =999, num_2 = 999):
    output_list = [1]
    min_value = 1
    if min_value > 1000:
        min_value = num_1 * num_2 / 100 * 50 # 50%
    elif min_value > 10000:
        min_value = num_1 * num_2 / 100 * 80 # 70%
    elif min_value > 100000:
        min_value = num_1 * num_2 / 100 * 90 # 90%


    for num1 in range(num_1, 0, -1):
        for num2 in range(num_2, 0, -1):
            output = num1 * num2
            if str(output) == str(output)[::-1]:
                output_list.append(output)
                break
            if output < min_value: # optimalization: if mul operation value is less than XX % of max then break
                break

    return max(output_list)



#print(palindromic_num_from_mul_of_two_num(99, 99))