class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        ans = 0
        repeat_char = set()
        for right in range(len(s)):
            while s[right] in repeat_char:
                repeat_char.remove(s[left])
                left += 1
            repeat_char.add(s[right])
            
            ans = max(ans, right - left + 1)

        return ans