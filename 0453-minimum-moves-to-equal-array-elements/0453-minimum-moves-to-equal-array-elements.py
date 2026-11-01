class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_element = min(nums)
        return sum(num - min_element for num in nums)
        