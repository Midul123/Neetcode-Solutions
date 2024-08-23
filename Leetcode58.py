#Leetcode58
def lengthOfLastWord(str):
        words= str.split()
        reverse=words[::-1]
        return(len(reverse[0]))
print(lengthOfLastWord("   fly me   to   the moon  "))