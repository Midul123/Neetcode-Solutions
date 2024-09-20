#Leetcode11
def maxArea(height):
    r=len(height)-1
    l=0
    maxArea=0
    while l!=r:
        area= min(height[l],height[r]) * (r-l)
        maxArea=max(area, maxArea)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return maxArea
print(maxArea([1,8,6,2,5,4,8,3,7]))