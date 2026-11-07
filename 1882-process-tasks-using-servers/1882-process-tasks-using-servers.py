class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:

        # approching two priority queues ideas one with the weight index and other one with the time of finishing index idea and then simulating 

        busy = list()
        
        idle = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(idle)

        ts = 0

        def release():  # release function once a server finish prcessing a task it goes back to the idle queue from the busy queue 
            while busy and busy[0][0] <= ts:
                _, idx = heapq.heappop(busy)
                heapq.heappush(idle, (servers[idx], idx))

        ans = list() # answer list which contains the indx of the servers which will be processing the tasks in the tasks queue


        for i, task in enumerate(tasks): # iteration over the task array
            ts = max(ts, i)
            release()
            if not idle:
                ts = busy[0][0]
                release()
            _, idx = heapq.heappop(idle)
            ans.append(idx)
            heapq.heappush(busy, (ts + task, idx))
        return ans # final answer
        