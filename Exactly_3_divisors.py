# Given number in range has exactly 3 divisors
# First we will check is the given number is prime or not
from math import sqrt


def isPrime(num):
    if num == 0 or num == 1:
        return False
    if num % 2 == 0 or num % 3 == 0:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(5, int(sqrt(num))+1, 6):
        if(num % i == 0 or num % (i+2) == 0):
            return False
    return True


def exactly3divisors(num):
    #If we check for various inputs and observe answer we can find they all are square of prime number 
    if num < 4:
        return 0
    if num >= 4 and num <= 8:
        return 1
    count = 2
    for i in range(5, int(sqrt(num))+1, 6):#Square root ensure that square of prime is in given number 
        if isPrime(i):#So we are checking for prime 
            count += 1
        if isPrime(i+2) and (i+2) <= sqrt(num):
            count += 1
    #As we use above method for finding square root we just simply modifiying the method          
    return count


print(exactly3divisors(25)) 

