# Question 1:
# write a function that returns all prime numbers from a given list
# of integers where the max value in the list cannot exceed 101


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

# length of test list
n=101
test_list=list(range(1,n+1))
print("before: ",test_list)


# Selection of Prime Numbers
def selectio_of_prime(L):
    return(list(filter(lambda s: is_prime(s) != False, L)))

# list of Prime Numbers
pn_list=selectio_of_prime(test_list)
print("after: ", pn_list)

