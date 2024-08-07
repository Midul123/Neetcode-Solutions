#Leetcode1071
import math
def gcdOfStrings(str1, str2):
    if str1+str2 != str2+str1:
        return ""
    #GCD finds the greatest common divisor length between two strings or integers
    gcd_lengh= math.gcd(len(str1), len(str2))
    return str1[:gcd_lengh]

print(gcdOfStrings("ABCABC", "ABC"))

