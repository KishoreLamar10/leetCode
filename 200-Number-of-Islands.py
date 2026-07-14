class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        cnt = 0
        directions = [[-1,0], [0,1], [1,0], [0,-1]]
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(ROWS) and nc in range(COLS) and (nr,nc) not in visit and grid[nr][nc] == "1"):
                        q.append((nr,nc))
                        visit.add((nr,nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == "1" and (r,c) not in visit):
                    bfs(r,c)
                    cnt += 1
        
        return cnt
