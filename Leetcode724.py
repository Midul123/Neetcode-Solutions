#Leetcode724
def pivotIndex(nums):
    psNums=[0] *len (nums)
    psNums[0]=nums[0]

    for i in range(1,len(nums)):
        psNums[i]= psNums[i-1] + nums[i]
    
    if psNums[-1]-psNums[0]==0:
        return 0

    for i in range(1, len(nums)):
        if psNums[i-1]==psNums[-1]-psNums[i]:
            return i

    return -1
print(pivotIndex([1,7,3,6,5,6]))