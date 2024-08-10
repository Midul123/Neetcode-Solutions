#Leetcode283
def moveZeroes(nums):
    last0 = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last0] = nums[i]
            last0+=1

    for i in range(last0, len(nums)):
        nums[i]=0    
    return nums
print(moveZeroes([0,1,0,3,12]))