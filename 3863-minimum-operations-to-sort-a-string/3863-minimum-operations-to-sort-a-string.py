class Solution:
    def minOperations(self, s: str) -> int:

        # THE COMMENTS IN THIS CODE IS WRITTEN FOR THE GITHUB CODE SUBMISSON AS WELL
        # explanatory comments are included for readability and future reference's as well

        n = len(s)
        
        max_ = max(s)
        mini_ = min(s)

        # we are going to divide the problem into some cases 

        if all(a <= b for a, b in zip(s, s[1:])):  # this is the case for the already sorted string in nondecreasing order 
            return 0

        if n == 2:   # for length 2 string which is not sorted in non decresing order it is always impossible to sort in that order
            return -1
        
        # A case where minimum or maximum of the of the string occurs at the start or end we can sort it using one operation  
        if s[0] == mini_  or s[-1] == max_:
            return 1
        
        # A case where minimum or maximum lies in the middle of the string then it takes onlt two operations to sort it 
        for i in range(1, n - 1):
            if s[i] == mini_ or s[i] == max_:
                return 2

        # for the last case largest element comes at the start and the smallest element comes at the last 
        # it takes only three operations     
        return 3 

