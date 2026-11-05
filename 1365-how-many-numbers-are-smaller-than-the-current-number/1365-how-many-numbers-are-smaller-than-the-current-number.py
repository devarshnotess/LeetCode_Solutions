class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        # combining the idea of sorting and original indices 

        frequency_array = []
        for i in range(len(nums)):
            frequency_array.append((nums[i], i))
        frequency_array.sort()

        answer = [0] * len(nums) # Final answer array
        
        answer[frequency_array[0][1]] = 0

        for j in range(1, len(frequency_array)):
            if frequency_array[j][0] == frequency_array[j - 1][0]:
                answer[frequency_array[j][1]] = answer[frequency_array[j - 1][1]]
            else:
                answer[frequency_array[j][1]] = j
        return answer # Final answer
        

                



            