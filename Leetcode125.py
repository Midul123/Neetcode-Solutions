#Leetcode125
def isPalindrome(str):
    clean = ""
    reverse= ""
    for char in str:
        if char.isalnum():
            clean+=char.lower()
    
    for i in range(len(clean)-1, -1 ,-1):
        reverse+=clean[i]
    
    return clean==reverse

print(isPalindrome("A man, a plan, a canal: Panama"))
