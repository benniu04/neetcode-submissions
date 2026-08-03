class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS, COLS = len(board), len(board[0])
        queue = collections.deque()

        def bfs(r, c):
            board[r][c] = "E"
            queue.append((r,c))

            while queue:
                r, c = queue.popleft()

                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
                        board[nr][nc] = "E"
                        queue.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                is_boundary = r in (0, ROWS - 1) or c in (0, COLS - 1)
                if is_boundary and board[r][c] == "O":
                    bfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
