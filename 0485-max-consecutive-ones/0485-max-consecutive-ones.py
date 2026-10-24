class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        current_count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_count += 1
            else:
                ans = max(ans, current_count)
                current_count = 0

        ans = max(ans, current_count)
        
        return ans 


