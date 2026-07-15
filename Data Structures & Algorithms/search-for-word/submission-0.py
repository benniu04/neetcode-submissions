class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(row, col, i):
            if i == len(word):
                return True
            if (row < 0 or row >= rows or 
            col < 0 or col >= cols or (row, col) in visited
            or board[row][col] != word[i]):
                return
            visited.add((row, col))
            res = (dfs(row + 1, col, i + 1) or 
                  dfs(row - 1, col, i + 1) or
                  dfs(row, col + 1, i + 1) or
                  dfs(row, col - 1, i + 1))
            visited.remove((row, col))
        
            return res
    
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False


            