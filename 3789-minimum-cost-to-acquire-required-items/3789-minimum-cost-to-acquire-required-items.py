class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        # Option 1: Buy only separate items
        opt1 = need1 * cost1 + need2 * cost2
        
        # Option 2: Buy only bundle items (Type 3)
        opt2 = costBoth * max(need1, need2)
        
        # Option 3: Buy max possible bundles, then cover leftovers with individual items
        mn = min(need1, need2)
        opt3 = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(opt1, opt2, opt3)