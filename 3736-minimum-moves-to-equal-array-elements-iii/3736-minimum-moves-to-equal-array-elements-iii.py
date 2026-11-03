class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        # We need to make each element equal so by one operation you can increase one element by value one so each element we have to make equal to the maximum value of the array 

        mx = max(nums)
        number_of_operations = 0
        for i in range(len(nums)):
            number_of_operations += abs(mx - nums[i]) # add the number_of_operations for each element and then add them in single variable
        
        return number_of_operations # Final answer
        
