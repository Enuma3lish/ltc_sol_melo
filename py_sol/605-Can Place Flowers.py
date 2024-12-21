from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed+[0]
        N= len(flowerbed)
        res = 0
        for i in range(1,N-1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1] ==0:
                res+=1
                flowerbed[i] = 1
        return res >= n
    
res = canPlaceFlowers([0,0,1,0,1], 1)
print(res)