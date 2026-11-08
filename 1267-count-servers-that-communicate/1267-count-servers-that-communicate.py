class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        # In this approach we are just first counting how many servers are there in the resepective rows and columns

        if not grid:
            return 0
        row_counts =[0] * len(grid) # row counts for each indexed row how many servers are there in that row
        col_counts = [0] * len(grid[0]) # column counts for each indexed columns how many servers are there in that column

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1: # for any cell we increse the number of servers for that specific row and column
                    row_counts[row] += 1
                    col_counts[col] += 1
        communicable_servers_count = 0 # count for how many servers can communicate with each other


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    if col_counts[col] > 1 or row_counts[row] > 1: # if the count for specific row or column's servers is greater than 1 then we can have the communicable servers in the count

                        communicable_servers_count += 1

        return communicable_servers_count # final count of the servers that can communicate with each other
        
