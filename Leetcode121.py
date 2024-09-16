#Leetcode121
def maxProfit(prices):
    smallest = float('inf')
    maxProfit = 0
    for price in prices:
        if price < smallest:
            smallest=price
        potentialProfit=price-smallest
        if potentialProfit>maxProfit:
            maxProfit=potentialProfit
    return maxProfit
print(maxProfit([7,1,5,3,6,4]))