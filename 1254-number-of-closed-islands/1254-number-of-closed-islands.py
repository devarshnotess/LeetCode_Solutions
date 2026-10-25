class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        rows = len(grid)
        columns = len(grid[0])

        answer = 0

        visited_cells = [[False] * columns for i in range(rows)]

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 0 and not visited_cells[i][j] and self.bfs(i, j, rows, columns, grid, visited_cells):
                    answer += 1
        return answer

    
    def bfs(self, p: int, q: int, rows: int, columns: int, grid: List[List[int]], visited_cells: List[List[bool]]) -> bool:

        d = deque([(p, q)])

        visited_cells[p][q] = True
        cell = True

        direction_x = [0, 1, 0, -1]
        direction_y = [-1, 0, 1, 0]

        while d:
            p, q = d.popleft()

            for i in range(4):
                r, c = p + direction_x[i], q + direction_y[i]
                if r < 0 or r >= rows or c < 0 or c >= columns: # boundry cell condition
                    cell = False
                elif grid[r][c] == 0 and not visited_cells[r][c]:
                    d.append((r, c))
                    visited_cells[r][c] = True

        return cell


        
        
