class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_map = defaultdict(int)
        i , j = 0, 0
        ans = 0

        while j < len(s):
            window_map[s[j]] += 1
            while window_map[s[j]] > 1:
                window_map[s[i]] -= 1
                if window_map[s[i]] == 0:
                    window_map.pop(s[i], None)
                i+= 1
            ans = max(ans, j - i + 1)
            j += 1
        
        return ans
            
        