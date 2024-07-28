#leetcode 3005
from collections import defaultdict
def maxFrequencyElements(nums):
    #use default dictiornary to set default value of 0
    output = 0
    frequency = defaultdict(int)
    
    for num in nums:
        frequency[num] +=1
    
    max_value = max(frequency.values())

    for key, value in frequency.items():
        if max_value==value:
            output+=value 
    return output

print(maxFrequencyElements([1,2,2,3,1,4]))