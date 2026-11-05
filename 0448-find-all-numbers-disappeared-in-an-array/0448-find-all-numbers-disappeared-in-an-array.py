class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:

        #frequency counting approach
        
        frequency_array = [0] * len(nums)
        answer = []
        for i in range(len(nums)):
            frequency_array[nums[i] - 1] += 1
        for i in range(len(frequency_array)):
            if frequency_array[i] == 0:
                answer.append(i + 1)
            else:
                continue
        return answer
        