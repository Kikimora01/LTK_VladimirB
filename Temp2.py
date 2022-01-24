

class Solution(object):
        underTen = ["", "One", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine"]
        underTwenty = ["", "Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen",
                 "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        underHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def numberToWords(self, num):
           sig=""
           if num<0:
              sig="Minus "
           num=abs(num)
           if num == 0:
              return "Zero"
           answer=self.helper(num)
           return  sig+answer

        def helper(self, num):
           result=""
           if num < 10:
              result=Solution.underTen[num]
           elif num < 20:
              result=Solution.underTwenty[num-9]
           elif num < 10**2:
              result=Solution.underHundred[num // 10]+ " "+self.helper(num % 10)
           elif num < 10**3:
              result=self.helper(num // 10**2) + self.aand(" Hundred ",num)+ self.helper(num % 10**2)
           elif num < 10**6:
              result = self.helper(num // 10**3) + self.aand(" Thousand ",num)+ self.helper(num % 10**3)
           elif num < 10**9:
             result = self.helper(num // 10**6) + self.aand(" Million ",num)+ self.helper(num % 10**6)
           else:
              result = self.helper(num // 10**9) + self.aand(" Billion ",num)+ self.helper(num % 10**9)
           return  result.strip()


# add  And
        def aand(self,str,num):
             s =str+ "And "
             if num % 100 == 0:
                      s = str
             return s

# End  of Class Solution
##################

# creation of object
ob = Solution()

# Examples

print(512,"-> ",ob.numberToWords(512))
print(7835271,"-> ",ob.numberToWords(7835271))

n1=7
n2=39
n3=302
n4=7654
n5=60034
n6=720540

n7=1234000
n8=23045012
n9=700340323

print(n1,"-> ",ob.numberToWords(n1))
print(n2,"-> ",ob.numberToWords(n2))
print(n3,"-> ",ob.numberToWords(n3))
print(n4,"-> ",ob.numberToWords(n4))
print(n5,"-> ",ob.numberToWords(n5))
print(n6,"-> ",ob.numberToWords(n6))
print(n7,"-> ",ob.numberToWords(n7))
print(n8,"-> ",ob.numberToWords(n8))
print(n9,"-> ",ob.numberToWords(n9))
print(-n9*4,"-> ",ob.numberToWords(-n9*4))


print(1500,"-> ",ob.numberToWords(1500))

print(200,"-> ",ob.numberToWords(200))
print(201,"-> ",ob.numberToWords(201))
print(210,"-> ",ob.numberToWords(210))
print(211,"-> ",ob.numberToWords(211))
print(220,"-> ",ob.numberToWords(220))

print(10,"-> ",ob.numberToWords(10))
print(11,"-> ",ob.numberToWords(11))
print(12,"-> ",ob.numberToWords(12))
print(19,"-> ",ob.numberToWords(19))
print(20,"-> ",ob.numberToWords(20))

print(0,"-> ",ob.numberToWords(0))
print(-27,"-> ",ob.numberToWords(-27))
print(1001,"-> ",ob.numberToWords(1001))
print(10001,"-> ",ob.numberToWords(10001))
print(100001,"-> ",ob.numberToWords(100001))
print(1021,"-> ",ob.numberToWords(1021))
print(1100,"-> ",ob.numberToWords(1100))
print(1321,"-> ",ob.numberToWords(1321))

print(1007001,"-> ",ob.numberToWords(1007001))
print(100000001,"-> ",ob.numberToWords(100000001))
print(10000000001,"-> ",ob.numberToWords(10000000001))