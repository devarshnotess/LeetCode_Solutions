class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        inc_length = dec_length = max_length = 1

        for pos in range(len(nums) - 1):
            if nums[pos + 1] > nums[pos]:
                inc_length += 1
                dec_length = 1
            elif nums[pos + 1] < nums[pos]:
                dec_length += 1
                inc_length = 1
            else:
                inc_length = dec_length = 1 # for equal (nums[pos + 1] == nums[pos])

            max_length = max(max_length, inc_length, dec_length)
        
        return max_length # final answer

  




