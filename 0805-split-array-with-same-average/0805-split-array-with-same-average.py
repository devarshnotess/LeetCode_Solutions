class Solution:
    def splitArraySameAverage(self, nums):
        
        from fractions import Fraction
        N = len(nums)
        S = sum(nums)
        A = [z - Fraction(S, N) for z in nums]

        if N == 1: return False

        left = {A[0]}

        for i in xrange(1, N/2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left: return True

        right = {A[-1]}
        for i in xrange(N/2, N - 1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right: return True
    
        sum_left = sum(A[i] for i in xrange(N / 2))
        sum_right = sum(A[i] for i in xrange(N/2, N))
    
        return any(-ap in right and (ap, -ap) != (sum_left, sum_right) for ap in left)
        