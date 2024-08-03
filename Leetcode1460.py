#Leetcode1460
from collections import defaultdict
def canBeEqual(target, arr):
        tar_count = defaultdict(int)
        arr_count = defaultdict(int)

        if len(target) != len(arr):
            return False

        for number in range(len(target)):
            tar_count[target[number]]+=1
            arr_count[arr[number]]+=1


        return(tar_count==arr_count)
print(canBeEqual([1,2,3,4], [2,4,1,3]))