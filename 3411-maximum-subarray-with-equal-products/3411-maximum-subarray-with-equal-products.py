class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd

        result = 2
        product_value = 1
        n = len(nums)
        start, end = 0,0

        while end < n:
            while gcd(product_value, nums[end]) > 1:
                product_value //= nums[start]
                start += 1
            product_value *= nums[end]
            result = max(result, end - start + 1)
            end += 1
        return result
