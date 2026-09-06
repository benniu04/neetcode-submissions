class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        new_stones = [-s for s in stones]
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            first = heapq.heappop(new_stones)
            second = heapq.heappop(new_stones)

            if first != second:
                diff = first - second
                heapq.heappush(new_stones, diff)
        
        new_stones.append(0)
        return abs(new_stones[0])
            
