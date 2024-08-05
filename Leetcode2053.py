#Leetcode2053
from collections import defaultdict
from collections import Counter
def kthDistinct(arr, k):
        frequency = defaultdict(int)
        frequency=Counter(arr)
        distinct = []
        for key, value in frequency.items():
            if value==1:
                distinct.append(key)
            
        if len(distinct) >= k:
            return distinct[k-1]
        else:
            return""
print(kthDistinct(["d","b","c","b","c","a"], 2))