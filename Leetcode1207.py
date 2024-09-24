#Leetcode1207
def uniqueOccurrences(arr):
        occ= {}
        occArr=[]
        for num in arr:
            if num in occ:
                occ[num]+=1
            else:
                occ[num]=1
        for num in occ.values():
            occArr.append(num)
        occSet=set(occArr)
        if len(occArr)==len(occSet):
            return True
        else:
            return False
print(uniqueOccurrences([1,2,2,1,1,3]))