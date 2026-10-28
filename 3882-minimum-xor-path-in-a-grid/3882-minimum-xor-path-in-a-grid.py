class Solution:
    def minCost(self, grid: list[list[int]]) -> int:

        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        # The main idea for this problem is the dynaminc programming 
        # means we check all possible paths and see which paths leads us the minimum value of the all values consecutive xors operation 
        rows, columns = len(grid), len(grid[0])

        dp = [[set() for _ in range(columns)] for _ in range(rows)]  # here we are creating a two dimensional dp array and stores the values of each path 

        dp[0][0].add(grid[0][0])

        for i in range(rows):
            for j in range(columns):

                if i == 0 and j == 0: # if we reach the boundry of the grid or just intial element if just ignore it because it it alredy present in the dp and have already taken it as a starting value as xor 
                    continue
                
                current_set = set()

                if i > 0: # current cell's above wether it exists checking condition 
                    for xor_value in dp[i - 1][j]:
                        current_set.add(xor_value ^ grid[i][j]) # if it exists we take the xor of the current grid element

                if j > 0: # current cell's left wether its exists checking condition
                    for xor_value in dp[i][j - 1]:
                        current_set.add(xor_value ^ grid[i][j]) # if it exists we take the xor of the current grid elements


                dp[i][j] = current_set # put it as value of that dp array's unique set 

        return min(dp[rows - 1][columns - 1]) # output the minimum of the last cell's set's minimun is the minimum answer obtained from the all possible path checking
