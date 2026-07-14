class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1), (0,-1), (1,0), (-1, 0)]

        max_area = 0

        def bfs(r, c):
            q = deque()
            area = 0
            grid[r][c] = 0
            q.append((r, c))
            area += 1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= rows or c + dc >= cols or grid[r+dr][c+dc] == 0:
                        continue
                    else:
                        grid[r+dr][c+dc] = 0
                        q.append((r+dr, c+dc))
                        area += 1
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                else:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
                
        return max_area