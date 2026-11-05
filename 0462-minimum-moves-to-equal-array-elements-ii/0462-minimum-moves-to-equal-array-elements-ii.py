class Solution:
    def minMoves2(self, nums: list[int]) -> int:

        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        # we just want to find the minimum number of operations to make array elements equal 
        nums.sort()

        n = len(nums)
        median = nums[n // 2]
        ans = 0

        for x in nums:
            ans += abs(x - median)
        return ans # final answer

        
