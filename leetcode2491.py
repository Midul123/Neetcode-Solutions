#leetcode2491
def dividePlayers(skill):
    pairs=[]
    skills = sorted(skill)
    l=len(skills)-1
    r=0
    output = 0
    while r<l:
        pairs.append((skills[r],skills[l]))
        r+=1
        l-=1
    sums=[]
    for pair in pairs:
        sums.append(sum(pair))
    sums=set(sums)
    if len(sums)!= 1:
        return -1
    else:
        for pair in pairs:
            output+=pair[0] * pair[1]            
    return output
print(dividePlayers([3,2,5,1,3,4]))