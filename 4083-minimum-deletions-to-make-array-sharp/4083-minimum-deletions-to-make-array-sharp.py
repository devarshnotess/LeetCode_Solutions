class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ans += 1
            else:
                continue
        return ans  
