#Leetcode9
def isPalindrome(x):
    toStr = str(x)
    reverse = toStr[::-1]
    if reverse==toStr:
        return True
    else:
        return False

print(isPalindrome(-121))    
