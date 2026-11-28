class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
            # meet in the middle way of doing the computation
        def helper(half_rods):
            states = set()
            states.add((0,0))
            for r in half_rods:
                new_states = set()
                for left, right in states:
                    new_states.add((left + r, right))
                    new_states.add((left, right + r))
                states |= new_states

            dp = {}
            for left, right in states:
                dp[left - right]  = max(dp.get(left - right, 0), left) # here we take the same difference's maximum height billboard

            return dp

        n = len(rods)
        first_half = helper(rods[: n // 2])
        second_half = helper(rods[n // 2: ])

        answer = 0

        for diff in first_half:
            if -diff in second_half:
                answer = max(
                    answer, first_half[diff] + second_half[-diff] # here we simply check wether there is some -diff exists in the second half
                    )
        return answer  # final answer
        
