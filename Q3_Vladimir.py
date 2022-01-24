# Question 3:
# write a function that takes a list character sequences, removes all non-alphanumeric
# characters from these,
# one-hot encodes the sequences and returns the result

# https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
# Machine learning algorithms cannot work with categorical data directly.
# Categorical data must be converted to numbers.

# https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
# https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/

import re


# function for removing non-alphanumeric from list of characters strings
# using regular expression
def rem_nonan(str):
    return(re.sub(r'[\W_]+', '', str))

# example of list
l1=["$^a#1","a4","@@@a1$%","!a&2","!@#$%^a**3", '!^&a*&^%$#@!4']

# removing non-an
l2=[rem_nonan(s) for s in l1]
print(l2)


# to remove duplicated
# from list
l3 = []
for i in l2:
        if i not in l3:
            l3.append(i)

print(l3)

# sorting of list
l3.sort()
print(l3)

def csTonh(l):
    n=len(l)
    result=[0]*n
    for i in range(0,n):
        foo=[0]*n
        foo[i]=1
        result[i]=foo
        print(l[i],"->",foo)
    return result


h=csTonh(l3)

print(h)

# or in one function

def for_LTK(l1):
    l2 = [rem_nonan(s) for s in l1]
    l3 = []
    for i in l2:
        if i not in l3:
            l3.append(i)
    l3.sort()
    answer = csTonh(l3)
    return answer

h=for_LTK(l1)
print(h)


