#Leetcode1894
def chalkReplacer(chalk, k):
        total_chalk = sum(chalk)
        
        # Reduce k by full cycles
        k = k % total_chalk
        
        # Find which student will need to replace the chalk
        for i in range(len(chalk)):
            if k < chalk[i]:
                return i
            k -= chalk[i]
print(chalkReplacer([3,4,1,2], 25))
    