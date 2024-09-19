#Leetcode1004
def longestOnes(nums, k):
    max_w=0
    num_zeros=0
    l=0
    for i in range(len(nums)):
        if nums[i]==0:
            num_zeros+=1
        while num_zeros>k:
            if nums[l]==0:
                num_zeros-=1
            l+=1
        w=i-l+1
        max_w=max(w,max_w)

    return max_w

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))