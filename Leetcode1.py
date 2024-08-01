#Leetcode1
def twoSum(nums, target):
    mapp ={}
    for i, n in enumerate(nums):
        difference = target - n
        if difference in mapp:
            return[mapp[difference], i]
        mapp[n] = i

print(twoSum([2,7,11,15], 9))