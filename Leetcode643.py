#Leetcode643
def findMaxAverage(nums,k):

    maxAvg=sum(nums[:k])
    total=maxAvg

    for i in range(len(nums)-k):
        maxAvg-=nums[i]
        maxAvg+=nums[i+k]
        total = max(total, maxAvg)
    
    return(total/k)
print(findMaxAverage([1,12,-5,-6,50,3], 4))
