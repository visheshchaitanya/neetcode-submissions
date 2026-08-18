from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def helper(curr_index: int, is_bought: bool):
            if curr_index >= len(prices):
                return 0

            if is_bought:
                return max(
                    prices[curr_index] + helper(curr_index + 2, False),
                    helper(curr_index + 1, True)
                )

            else:
                return max(
                    -prices[curr_index] + helper(curr_index + 1, True),
                    helper(curr_index + 1, False)
                )

        return helper(0, False)