class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        
        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well
    

        # Here we just want to find the number of islands whose total value is divisible by k
        # We simply applay depth first search

        rows, columns = len(grid), len(grid[0])
        directions_4 = (-1, 0, 1, 0, -1) # directions 


        def dfs(i: int, j: int) -> int:
            final = grid[i][j]
            grid[i][j] = 0 # after visiting the value of that cell is made zero so that we do not visit again 

            for e in range(4):
                x, y = i + directions_4[e], j + directions_4[e + 1]  # In each directions traversal
                if 0 <= x < rows and 0 <= y < columns and grid[x][y] > 0:
                    final += dfs(x, y)  # once we find the island we just sum its value we are just finding its total value
            return final  # we return the final value for the specific cell
        
        return sum(
            grid[i][j] > 0 and dfs(i, j) % k == 0 # Now we check wether the the island's total value is divisible by k
            # if it is divisible by k then we add it in the count of answer
            for i in range(rows)
            for j in range(columns)
        )