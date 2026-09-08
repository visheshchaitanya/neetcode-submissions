class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def backtrack(index, curr, total):
            if total == target:
                ans.append(list(curr)) 
                return
            if total > target:
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()

        backtrack(0, [], 0)
        return ans