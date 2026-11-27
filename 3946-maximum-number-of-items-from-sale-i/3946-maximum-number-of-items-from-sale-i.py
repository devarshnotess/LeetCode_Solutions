class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
            # Dynamic programming (0 - 1 Knapsack) 
        s = [0] * (budget + 1)

        mn = min(price for _, price in items)

        for factor, price in items:
            count = sum( 
                1 for other_factor, _ in items if other_factor % factor == 0
            )

            for j in range(budget, price - 1, -1):

                if s[j - price] + count > s[j]:
                    s[j] = s[j - price] + count

        return max( s[j] + (budget - j) // mn for j in range(budget + 1))
