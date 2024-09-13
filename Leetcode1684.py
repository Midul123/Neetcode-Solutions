#Leetcode1684
def countConsistentStrings(allowed, words):
        counter = 0
        allowed=set(allowed)
        for word in words:
            allAllowed= True
            for char in word:
                if char not in allowed:
                    allAllowed= False
            if allAllowed:
                counter+=1
        return counter
print(countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))