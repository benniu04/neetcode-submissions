class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sorted_elements = sorted(frequency.keys(), reverse=True, key=frequency.get)

        return sorted_elements[:k]
