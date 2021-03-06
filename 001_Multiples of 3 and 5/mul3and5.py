'''
author: a5892731
date: 2021-01-30

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

__________________________________________
try to run it on Git Bash :)

'''

class Multiples_3_and_5(object):
    version = "1.00"
    div_range = 1000

    def __init__(self):
        self.sum_of_dividers = 0
        self.dividers = []

    def find_dividers_of_3_or_5(self):
        output =  [number for number in range(self.div_range)
                if (number % 3 == 0 or number % 5 == 0) and number != 0]

        #print(">>>> Dividors of 3 and 5 in range {} are:\n {}".format(div_range, output))
        self.dividers = output

    def find_sum_of_dividers(self):
        sum = 0
        for divider in self.dividers:
            sum += divider
        self.sum_of_dividers =  sum
        #print("Sum off dividers list is: {}".format(sum))

    def clear(self):
        self.sum_of_dividers = 0
        self.dividers = ()

#------------------------------------------------------------------


output = Multiples_3_and_5()
print("\nSum off dividers list is: {} in range {}".format(output.sum_of_dividers, output.div_range))
output.div_range = 100
output.find_dividers_of_3_or_5()
output.find_sum_of_dividers()
print("\nSum off dividers list is: {} in range {}".format(output.sum_of_dividers, output.div_range))
print("Dividors of 3 or 5 in range {} are:\n{}".format(output.div_range, output.dividers))