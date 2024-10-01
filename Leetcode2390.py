#Leetcode2390
def removeStars(s):

    removed = []
    for i in s:
        if i == '*':
            removed.pop()
        else:
            removed.append(i)

    return ''.join(removed)

print(removeStars("leet**cod*e"))