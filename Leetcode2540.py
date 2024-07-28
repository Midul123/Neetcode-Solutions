#Leetcode2540
def getCommon(nums1, nums2):
    set1=set(nums1)
    common = -1
    for numbers in nums2:
        if numbers in set1:
            if common == -1 or numbers < common:
                common=numbers
    return common

print(getCommon([1,2,3],[2,4]))