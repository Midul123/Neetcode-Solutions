#Leetcode2215
def findDifference(nums1, nums2):
    #Solution with HashMap
    answer = [[], []]
    num1Map= {i:n for n,i in enumerate(nums1)}
    num2Map= {i:n for n,i in enumerate(nums2)}

    for i in range(len(nums1)):
        if nums1[i] not in num2Map.keys() and nums1[i] not in answer[0]:
            answer[0].append(nums1[i])

    for i in range(len(nums2)):
        if nums2[i] not in num1Map.keys() and nums2[i] not in answer[1]:
            answer[1].append(nums2[i])
            
    return answer

    #Solution with HashSet


    # set1=set(nums1)
    # set2=set(nums2)

    # answer1=list(set1-set2)
    # answer2=list(set2-set1)

    # return answer1, answer2

print(findDifference([1,2,3],[2,4,6]))