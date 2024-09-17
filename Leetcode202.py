#Leetcode202
def isHappy(n):
        trackN = []
        while n !=1:
            sumN = 0
            for i in str(n):
                sumN+=int(i)**2
            if sumN in trackN:
                return False
                
            trackN.append(sumN)
            n=sumN
        return True
print(isHappy(20))
