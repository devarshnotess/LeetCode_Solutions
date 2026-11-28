class Solution:
    def minAbsDifference(self, nums: list[int], goal: int) -> int:

        # Meet me in the middle approach 

        def dfs(i, current, arr, sums):
            if i == len(arr):
                sums.add(current)
                return 
            dfs(i + 1, current, arr, sums)
            dfs(i + 1, current + arr[i], arr, sums)
        
        sums1, sums2 = set(), set()

        dfs(0,0, nums[: len(nums)// 2], sums1) # generating all possible subsequence for the first half
        dfs(0,0, nums[len(nums)// 2 :], sums2) # generating all possible subsequence for the second half


        s2 = sorted(sums2) # here we do the sorting so we can perform the binary search 

        ans = 10**10

        for s in sums1:
            remain = goal - s
                # performing the binary search to find the closest possible value to goal
            i2 = bisect_left(s2, remain)
            if i2 < len(s2):
                ans = min(ans, abs(remain - s2[i2]))
            if i2 > 0:
                ans = min(ans, abs(remain - s2[i2 - 1]))
        return ans # final answer
        




                