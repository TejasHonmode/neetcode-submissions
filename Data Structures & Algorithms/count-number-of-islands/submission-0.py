class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        island_cnt = 0

        def bfs(r, c):
            q = deque()
            grid[r][c] = '0'
            q.append((r,c))

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= rows or c + dc >= cols or grid[r+dr][c+dc] == '0':
                        continue
                    else:
                        grid[r+dr][c+dc] = '0'
                        q.append((r+dr, c+dc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '0':
                    continue
                else:
                    island_cnt += 1
                    bfs(r,c)
        return island_cnt

                    


        