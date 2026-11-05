class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        
        frequency_array = [[x, 0] for x in range(1, len(nums)+ 1)]
        for i in range(len(nums)):
            frequency_array[nums[i] - 1][1] += 1
        frequency_array.sort(key = lambda x : x[1])

        return [frequency_array[-1][0], frequency_array[0][0]]