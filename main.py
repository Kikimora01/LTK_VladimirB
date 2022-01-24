# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Question #1

# Question # 2

class Solution(object):
less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
        "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

def numberToWords(self, num):
    if num == 0:
        return "Zero"
ans = ""
i = 0
while num > 0:
if num % 1000 != 0:
    ans = self.helper(num % 1000) + Solution.thousands[i] + " " + ans
    i += 1
    num //= 1000
return ans.strip()

def helper(self, n):
if n == 0:
    return ""
elif n < 20:
    return Solution.less_than_20[n] + " "
elif n < 100:
    return Solution.tens[n // 10] + " " + self.helper(n % 10)
else:
    return Solution.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)


ob = Solution()

print(ob.numberToWords(512))
print(ob.numberToWords(7835271))

# Global Array storing word for each digit
arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

print(arr)

# Question # 3

x = 23
print(x)
