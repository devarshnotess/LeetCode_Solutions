class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        # Here we approach the sliding window and sorting way using two pointer approach 
        logs.sort(key= lambda log: log[1])
        ids = sorted(range(len(queries)), key = lambda i : queries[i])
        ans = [0] * len(queries)
        count = [0] * (n + 1)
        left = right = active = 0

        for i in ids:
            q = queries[i]
            while right < len(logs) and logs[right][1] <= q:
                id = logs[right][0]
                if count[id] == 0:
                    active += 1
                count[id] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                id = logs[left][0]
                count[id] -= 1
                if count[id] == 0:
                    active -= 1  
                left += 1
            ans[i] = n - active
        return ans