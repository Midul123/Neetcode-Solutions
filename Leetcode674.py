#Leetcode674
def findLengthOfLCIS(nums):
    if not nums:
         return 0
    subsq=[]
    count=1
    n = len(nums)
    for i in range(n-1):
        if nums[i+1]>nums[i]:
                count+=1
        else:
            subsq.append(count)
            count=1
    subsq.append(count)
    return max(subsq)
print(findLengthOfLCIS([1,3,5,4,7]))