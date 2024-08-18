#Leetcode860
def lemonadeChange(bills):
    change = []

    for bill in bills:
        if bill == 5:
            change.append(bill)
        elif bill == 10:
            if 5 in change:
                change.remove(5)
            else:
                return(False)
                
            change.append(bill) 
        elif bill==20:
            if 5 in change and 10 in change:
                change.remove(5)
                change.remove(10)
                change.append(bill)
            elif change.count(5) >= 3:
                change.remove(5)
                change.remove(5)
                change.remove(5)
                change.append(bill)
            else:
                return(False)
                
    return True
print(lemonadeChange([5,5,5,10,20]))       