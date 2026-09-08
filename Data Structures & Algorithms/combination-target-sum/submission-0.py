class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def helper(index, curr, total):
            if total > target:
                return

            if index == len(nums):
                if total == target:
                    ans.append(curr[:])
                return

            helper(index + 1, curr, total)

            curr.append(nums[index])
            helper(index, curr, total + nums[index])
            curr.pop()

        helper(0, [], 0)
        return ans