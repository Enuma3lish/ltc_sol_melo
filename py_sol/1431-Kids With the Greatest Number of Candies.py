from typing import List


def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for cand in candies:
            temp = extraCandies+cand
            if max(candies) > temp:
                result.append(False)
            else:
                result.append(True)
        return result
result = kidsWithCandies([4,2,1,1,2], 1)
print(result)