class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        n = len(nums) 
        factors = []
        # Here we are just trying to find the numbers that divides the N(length of the array) in O(sqrt(n)) time

        for x in range(1, isqrt(n) + 1):
            if n % x == 0:
                factors.append(x)
                if n // x != x:
                    factors.append(n // x)

        sorted_array = sorted(nums)  # Final sorted array we will have.
        
        def function1(nums1, nums2):
            length1, length2 = len(nums1), len(nums2)

            # it stores the length of the longest matching prefix and suffix at each index
            result = [0] * length2
            
            s = 0

            for i in range(1, length2):
                # if element values do not match, we go back to a shorter matching prefix 
                while s > 0 and nums2[i] != nums[s]:
                    s = result[s - 1]
                # if it matches, move ahead the current matching prefix
                if nums2[i] == nums[s]:
                    s += 1
                
                # save the matching prefix length for the current index 
                result[i] = s

            s = 0  # we strart searching for nums2 in nums1 from the beginning
            for i in range(length1):
                # if on the mismatch, we use the prefix array to continue without again starting
                while s > 0 and nums1[i] != nums2[s]:
                    s = result[s - 1]
                
                # if it matches we just increse the length of the current match
                if nums1[i] == nums2[s]:
                    s += 1
                
                # If the entire pattern matches, nums2 is present in nums1
                if s == length2:
                    return True
            # pattern is not present 
            return False
        
        def function2(nums1, nums2):

            # Now we check if we can produce the nums2 by cyclic rotations of nums1
            # doubling the nums1 makes every cyclic rotaions appear as a subarrray
            # we use the function1 to check if nums2 is present in the nums1

            return function1(nums1 + nums1, nums2)

        ans = 0

        # iterating over the all  possible divisors of the N(length of the Array) 
        for i in factors:
            # dividing the array into subarrays of the length K

            for l in range(0, n, i):
                r = l + i - 1

                # now we just if the current block's cyclic rotations match the corresponding segement in the sorted array 

                if not function2(nums[l : r + 1], sorted_array[l : r + 1]):
                    break  # if the some segment do not match we just stop that whole branch of the K
            else:
                ans += i # if all blocks pass the check this block length is valid, then we just add it to the answer

        return ans
        # Final answer!

    