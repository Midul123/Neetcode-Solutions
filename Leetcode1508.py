#Leetcode1508
def rangeSum(nums, n, left, right):
    MOD = 10**9 + 7
    sum_subarray= []
    for start in range(n):
        for end in range(start, n):
            subarray = nums[start:end+1]
            subarray_sum = sum(subarray)
            sum_subarray.append(subarray_sum)
    sortedSub=sorted(sum_subarray)
    sumIndex=sortedSub[left-1:right]
    return sum(sumIndex) % MOD
print(rangeSum([1,2,3,4], 4 ,1 ,5))