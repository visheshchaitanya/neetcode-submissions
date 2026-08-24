class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for num in nums:
            heapq.heappush(pq, -num)
        
        ans = -1
        while k > 0:
            ans = heapq.heappop(pq)
            k -= 1
        
        return -ans



        