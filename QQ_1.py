# Question 1:
# write a function that returns all prime numbers from a given list
# of integers where the max value in the list cannot exceed 101

# https://www.quora.com/How-can-I-find-prime-numbers-in-a-list-in-Python

# predicate of Prime Number

def is_prime(n: object) -> object:
    if n <= 0:
        return False
    elif n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Example #1
a=is_prime(9)
b=is_prime(7)
print(a,b)

test_list=list(range(1,102))

print("before:" ,test_list)



def selectio_of_prime(L):
    return(list(filter(lambda s: is_prime(s) != False, L)))


pn_list=selectio_of_prime(test_list)

print("after: ", pn_list)

