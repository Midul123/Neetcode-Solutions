#Leetcode605
def canReplaceFlowers(flowerbed, n):
    counter=0
    for i in range(len(flowerbed)):
        prev= flowerbed[i-1] if i>0 else 0
        next=flowerbed[i+1] if i<len(flowerbed)-1 else 0

        if prev==0 and next ==0 and flowerbed[i]==0:
            flowerbed[i]=1
            counter+=1
                
        if counter>=n:
            return(True)
        else:
            return(False)

#Alternative way
# def canReplaceFlowers(flowerbed, n):
#     target = 0
#     if len(flowerbed)==1 and flowerbed[0]==0:
#         return True
#     for i in range(len(flowerbed)-1):
#         if i==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
#             flowerbed[i]=1
#             target+=1
#         if i==len(flowerbed)-2 and flowerbed[i]==0 and flowerbed[i+1]==0:
#             flowerbed[i+1]=1
#             target+=1
#         if flowerbed[i-1]==0 and flowerbed[i+1] == 0 and flowerbed[i]==0:
#             flowerbed[i]=1
#             target+=1
#         if target>=n:
#             return True
#         else:
#             return False 
        



print(canReplaceFlowers([1,0,0,0,1], 2))