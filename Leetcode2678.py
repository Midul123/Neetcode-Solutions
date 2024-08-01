#Leetcode2678
def countSeniors(details):
    output = 0
    for i in details:
        age = int(i[11:13])
        if age>60:
            output+=1
    return output

print(countSeniors(["7868190130M7522","5303914400F9211","9273338290F4010"]))