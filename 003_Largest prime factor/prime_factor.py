'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def largest_prime_factor_from_number(number):
    max_prime_number = 1

    if number <= 1:
        return None
    else:
        while number > 1:
            print(number)
            if prime_number_check(number) == True:
                max_prime_number = number
                break
            number -= 1
        return max_prime_number

def prime_number_check(number):
    divisors = 2  # every number have at least 2 divisors
    max_range = number
    if number > 10:
        max_range == 10 # if the number cant be divided by rest of numbers (higher than 10),
                                # it will never be devided unteal it reach it own value


    for divisor in range(2, max_range): # 1 is deleted because is always a divisor.
        if number % divisor == 0:
            divisors += 1
        if divisors > 2: #the prime number can be divided only by 1 and himself (2 divisors)
            return False
    return True



#---------------------------------



#print(">>>>>> " + str(largest_prime_factor_from_number(600851475143)))

#print(">>>>>> " + str(largest_prime_factor_from_number(13)))

