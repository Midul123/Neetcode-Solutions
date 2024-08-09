#Leetcode345
def reverseVowels(s):
    s_list = list(s)
    vowels = ['A','a','E','e','I','i','O','o','U','u']
    vowels_found = []
    for char in s_list:
        if char in vowels:
            vowels_found.append(char)
    vowels_found.reverse()

    pointer =0
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            s_list[i]=vowels_found[pointer]
            pointer+=1

    s=''.join(s_list)
    return s
print(reverseVowels("hello"))