import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / mid)
            
            if time_taken <= h:
                high = mid
            else:
                low = mid + 1

        return low
        