#Leetcode1431
def kidsWithCandies(candies, extraCandies):
    output = []
    greatest = max(candies)
    for i in range(len(candies)):
        candies[i]+=extraCandies
        if candies[i] >= greatest:
            output.append(True)
        else:
            output.append(False)
    return(output)    
print(kidsWithCandies([2,3,5,1,3], 3))