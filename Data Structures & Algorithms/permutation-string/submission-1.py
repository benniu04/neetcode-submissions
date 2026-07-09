from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if s1Count == window:
            return True
        
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1

            left_char = s2[i - len(s1)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]

            if window == s1Count:
                return True
        
        return False

        