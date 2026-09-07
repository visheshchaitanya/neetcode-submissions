class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(index, curr):
            if index == len(nums):
                ans.append(curr[:])
                return
            
            helper(index+1, curr)
            curr.append(nums[index])
            helper(index+1, curr)
            curr.pop()
        
        helper(0, [])
        return ans
        