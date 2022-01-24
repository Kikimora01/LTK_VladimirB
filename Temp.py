lower=1
upper=13

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                print(num)


def yes_prime(lower,upper):
    qq=[]
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                     qq.append(num)




print(yes_prime(1,101))


def prime(n):
    if n <= 0:
        return "Not defined"
    elif n == 1:
        return "Not prime"
    for i in range(2, n):
        if n % i == 0:
            return "not prime"
    return "prime"


def list_prime(lst):
    prime_list = []
    for i in lst:
        x = prime(i)
        if x == "prime":
            prime_list.append(i)
    return prime_list

l3=list(range(1,102))
print(list_prime([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list_prime(l3))


def this_prime(n):
    if n==0:
        continue
    elif n==1:
        continue




def is_prime(n):
     if n <= 0:
         continue
         elif
         n == 1:
                                     continue
                           for i in range(2, n):
                           if n % i == 0:
                               continue
                    return n


test_list1=[1,2,3,4,6,7,8,9,1,3,6,10,7,3,2,3,4,5,10,9,8,7,6,5,4,3,2,1]

h2=[is_prime(i) for i in test_list1]
