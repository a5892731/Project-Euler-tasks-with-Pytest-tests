'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def prime_num(prime_sequence_number):
    prime_number_counter = 0
    potential_prime_number = 2 # first prime number
    prime_list = ()

    if prime_sequence_number < 1:
        return None

    while True:
        if prime_number_check2(potential_prime_number, prime_list) == True:
            prime_number_counter += 1
            prime_list = prime_list + (potential_prime_number,)
        if prime_number_counter == prime_sequence_number:
            prime_number = potential_prime_number
            break
        potential_prime_number += 1

    return prime_number

def prime_number_check(number, prime_list):
    for divisor in range(2, number): # 1 is deleted because is always a divisor.
        if number % divisor == 0: #the prime number can be divided only by 1 and himself (2 divisors)
                                    #so if there is more, return false
            return False
    return True

def prime_number_check2(number, prime_list): # faster version
    divisors_list = prime_list  # if your number is not prime, then it can be divided by one of those numbers
    for divisor in divisors_list:
        if number % divisor == 0:  # the prime number can be divided only by 1 and himself (2 divisors) so if function finds another, then return false
            return False
    return True


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



#--------------------------------------------------------------------------
print(prime_num(100000)) #104743

#print(prime_num(1000)) #(1000, 7919),

#for i in range(1,101):
#    print(str(i) + " " + str(prime_num(i)))


