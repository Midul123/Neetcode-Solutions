#Leetcode1732
def largestAltitude(gain):
    altitude=[0]
    for i in range(len(gain)):
        altitude.append(altitude[i]+gain[i])
    
    return max(altitude)
print(largestAltitude([-5,1,5,0,-7]))
