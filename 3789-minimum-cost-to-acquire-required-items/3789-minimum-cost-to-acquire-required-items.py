class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if costBoth < (cost1 + cost2):
            if need1 >= need2:
                cost_1 = need2 * costBoth + abs(need1 - need2) * cost1 # for minimum part of need2
                cost_2 = need1 * costBoth # choosing that what if we buy maximum need1 part
            else:
                cost_1 = need1 * costBoth + abs(need2 - need1) * cost2 # for minimum part of need1
                cost_2 = need2 * costBoth # choosing that what if we buy maximum need2 part
            
            cost = min(cost_1, cost_2) # take the minimum of both the cases
        else:
            cost = need1 * cost1 + need2 * cost2 # In this case we check that total combine cost is lesser than the costBoth hence we buy individual quantities of type1 and type2 product
        
        return cost # Final answer

