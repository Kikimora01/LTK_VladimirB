# Question 2:
# write a function that takes an integer between negative one billion and
# positive one billion, including zero,
# and returns the english-language equivalent, including appropriate 'and's

# Using Prototype from
# https://www.tutorialspoint.com/integer-to-english-words-in-python-programming

## https://bohenan.gitbooks.io/leetcode/content/mathstring/237-integer-to-english-words.html
n1=7
n2=39
n3=302
n4=7654
n5=60034
n6=720540
n7=1234000
n8=23045012
n9=700340323

less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
        "Seventy", "Eighty", "Ninety"]
thousands = ["", "Thousand", "Million", "Billion"]

x=n9 // 100000000
print(x)


class Solution(object):
    belowTen = ["", "One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine"]
    belowTwenty = ["", "Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen",
                   "Sixteen", "Seventeen", "Eighteen","Nineteen"]
    belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"]
    less_than_20 = ["", "One", "Two", "Three", "Four", "Five", "Six",
                    "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
        "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]
    def numberToWords(self,num):
        if num == 0:
            return "Zero"
        ans = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                ans = self.helper(num % 1000) + Solution.thousands[i] + " " + ans
                i += 1
                print(num, ans,i) ################
                num //= 1000
                return ans.strip()

    def helper(self, n):
        if n == 0:
            return ""
        elif n < 20:
            return Solution.less_than_20[n] + " "
        elif n < 100:
            return Solution.tens[n // 10] + " " + self.helper(n % 10)
        elif n < 1000:
            return Solution.thousands[3] + " " + self.helper(3) ######
        else:
            return Solution.less_than_20[n // 100] + " Hundred " + self.helper(n % 100)

ob = Solution()

print(ob.numberToWords(n1))
print(ob.numberToWords(n2))
print(ob.numberToWords(n3))
print(ob.numberToWords(n4))
print(ob.numberToWords(n5))


print(ob.numberToWords(512))
print(ob.numberToWords(7835271))



print(ob.numberToWords(7100))

