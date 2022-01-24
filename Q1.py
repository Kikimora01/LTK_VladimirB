# Question 1: write a function that returns all prime numbers from a given list
# of integers where the max value in the list cannot exceed 101

def prinum(n):
        if n==0 :
            return "ha-ha1"  # continue
        elif n==1 :
            return "ha-ha2"  # continue
        elif n>1 :
                for i in range(2, n):
                    if i != 0:
                       return "ha-ha3" # continue
        else:
            return n

h7=prinum(7)
h9=prinum(9)
print(h7,h9)

a=[1,2,3,5,7]
b=[4,6,8,9,10]

l1=b
x=[1,2,3,4,6,7,8,9,10,7,3,2,3,4,5,10,9,8,7,6,5,4,3,2,1]
l2=x

for y in b:
    if y in x:
        x.remove(y)

print(x)

l3 = [s for s in l1 if s not
      in l2]

print(l1,l2,l3)

l4=list(filter(lambda s: s not in b, l2))
print(l4,l1)

def prime_pos_list(l2):
    return(list(filter(lambda s: s not in [4,6,8,9,10], l2)))


h=prime_pos_list(l2)

print(h)


