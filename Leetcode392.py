#Leetcode392
def isSubsequence(s,t):
        p1 = 0
        p2 = 0
        subs = ""
        while p1<len(s) and p2<len(t):
            if s[p1]== t[p2]:
                subs+=s[p1]
                p1+=1
            p2+=1
        return subs==s
print(isSubsequence("abc", "ahbgdc"))