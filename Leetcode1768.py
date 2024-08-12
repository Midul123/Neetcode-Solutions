#Leetcode1768
def mergeAlternately(word1, word2):
        w1 = list(word1)
        w2 = list(word2)
        result = ""

        min_len = min(len(w1), len(w2))

        for i in range(min_len):
            result+=w1[i]
            result+=w2[i]
            
        if len(w1)>len(w2):
            result+=''.join(w1[min_len:])
        elif len(word2) > len(word1):
            result+=''.join(w2[min_len:])
        return result   
print(mergeAlternately("abc", "pqr"))