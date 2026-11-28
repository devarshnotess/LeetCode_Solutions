class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        # This is very similiar to the problem  NO. 1755
        # here we also use the same technique  
        from bisect import bisect_left

        n = len(nums)// 2
        S = sum(nums)

        def dfs(i , count, current_sum, arr, res): # first we just generate certain number of combinations and also track how many elements we have chosen
            if i == len(arr):
                res[count].append(current_sum)
                return 
            dfs(i + 1, count, current_sum, arr, res) # Not including the element 

            dfs(i + 1, count + 1, current_sum + arr[i], arr, res) # including the element 
        
        left = [[] for _ in range(n + 1)] # dividing the input array into two subparts of the input
        right = [[] for _ in range(n + 1)]

        dfs(0, 0, 0, nums[: n], left)
        dfs(0,0,0 , nums[n :], right)


        for i in range(n + 1):
            right[i].sort() # sort the right array part so we can apply the binary search


        ans = float("inf")

        for k in range(n + 1):

            for x in left[k]:
                arr = right[n - k]
                target = (S - 2 * x) / 2

                index = bisect_left(arr, target)

                if index < len(arr):
                    ans = min(ans, abs(2*(x + arr[index]) - S))

                if index > 0:
                    ans = min(ans, abs(2 * (x + arr[index - 1]) - S))
        return ans # final answer
        




