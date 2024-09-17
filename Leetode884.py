#Leet884
def uncommonFromSentences(s1, s2):
    sen1=s1.split()
    sen2=s2.split()

    output=[]

    for word in sen1:
        if sen1.count(word)==1 and word not in output and word not in sen2:
            output.append(word)
        
    for word in sen2:
        if sen2.count(word)==1 and word not in output and word not in sen1:
            output.append(word)
    return output
print(uncommonFromSentences("apple apple", "banana"))