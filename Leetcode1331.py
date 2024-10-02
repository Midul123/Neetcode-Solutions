#Leetcode1331
def arrayRankTransform(arr):
    sortedArr = sorted(set(arr))
    indexMap= {i:n for n,i in enumerate(sortedArr)}
    output = []
    return [indexMap[num]+1 for num in arr]
print(arrayRankTransform([40,10,20,30]))