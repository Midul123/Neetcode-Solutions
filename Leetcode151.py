#Leetcode151
def reverseWords(s):
    split_s= s.split()
    reversed=[]
    for i in range(len(split_s)-1, -1, -1):
        reversed.append(split_s[i])

    reversed_s = ' '.join(reversed)
    return reversed_s
print(reverseWords("the sky is blue"))

#Simple version from chatgpt
# def reverseWords(s):
#     reverse = ' '.join(s.split()[::-1])
#     return reverse
# print(reverseWords("the sky is blue"))