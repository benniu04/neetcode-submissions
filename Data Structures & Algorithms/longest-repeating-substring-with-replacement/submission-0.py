class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        character_set = set(s)
        for c in character_set:
            curr = left = 0
            for right in range(len(s)):
                if s[right] == c:
                    curr += 1
                while (right - left + 1) - curr > k:
                    if s[left] == c:
                        curr -= 1
                    left += 1 

                ans = max(ans, right - left + 1)

        return ans