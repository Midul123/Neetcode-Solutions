
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


###
##FASTER SOLUTION
###
# def isPalindrome(s):
#     clean = []
#     for char in s:
#         if char.isalnum():
#             clean.append(char.lower())
#     clean_string = ''.join(clean)
#     reverse = clean_string[::-1]
#     return clean_string==reverse
# print(isPalindrome("A man, a plan, a canal: Panama"))