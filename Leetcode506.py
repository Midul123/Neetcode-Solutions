#Leetcode506
def findRelativeRanks(score):
    sortScore = sorted(score)
    sortScore.reverse()
    scoreIndex={n:i+1 for i,n in enumerate(sortScore)}
    output=[]
    for num in score:
        if scoreIndex[num]==1:
            output.append("Gold Medal")
        elif scoreIndex[num]==2:
            output.append("Silver Medal")
        elif scoreIndex[num]==3:
            output.append("Bronze Medal")
        else:
            output.append(str(scoreIndex[num]))
    return output
print(findRelativeRanks([5,4,3,2,1]))


