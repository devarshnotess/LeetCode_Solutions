class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        n = len(nums)
        if n == 1:   # It takes care of the base case if arrays length is one it is already sorted hence zero operations
            return 0

        zero_index = nums.index(0)  # first we take the index of the 0 the element 

        # Now we check wether the array is in the ascending order when we move to the right and descending order when we move to the left

        a1 = True  # ascending order
        a2 = True  # descending order

        for j in range(1, n):
            # maintaining the index ordering when we reach the end it shifts to the start of the array and stops the loop when it reaches the previous index of the zero_index means when it reaches the (zero_index - 1) 
            i = (zero_index + j) % n            
            current_value = nums[i]

            if current_value != j:   # the value of that index must match the index for ascending if not then the ascending order is not present
                a1 = False
            
            if current_value != n - j: # the value of that index must match the n - j for descending order if not then the descending order is not present
                a2 = False
            
            if not a1 and not a2: # if both the cases of ascending and descending is not present then there is no operations that can sort the array hence we return -1 
                return -1
        if a1:
            return min(zero_index, n - zero_index + 2)  # for ascending order take the minimum of the following two variables
        else:
            return min(n - zero_index, zero_index + 2) # for descending order take the minimum of the following two variables 
            

            
