class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        indices = []

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                indices.append(left + 1)
                indices.append(right + 1)
                break
            elif sum > target:
                right -= 1
            else:
                left += 1
                
        
        return indices