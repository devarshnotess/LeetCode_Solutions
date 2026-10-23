class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well


        # The problem is to find the largest K such that we can swap two elements if nums[i] & nums[j] = k
        # with that operation we can sort the whole array in non decreasing order
        # for K to satisfy this we k's set of bits must be part of element nums[i] and nums[j]'s set of bits 
        # Hence nums[i] & K = k, nums[j] & K = K, The largest K is just the collectively and operation of all elements that are not at their position meaning (nums[i] != i) 
         
        # By this K we can swap any two misplaced elements total three swapping operations, Hence we can sort the array

        n = len(nums)
        ans = -1

        for i in range(n):
            if nums[i] == i:
                continue
            ans = ans & nums[i]

        return 0 if ans == -1 else ans  # for the base case if array is already sorted operations must be zero

        
