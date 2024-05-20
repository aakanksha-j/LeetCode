from heapq import heappush, heappop

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        
        # time O(nlogn) for sorting
        # space O(N) - storing start, end and profit of each job - 3N space
        
        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(key = lambda x: x[0])
        
        maxProfit = 0
        heap = []
        
        for start, end, profit in jobs:
            while heap and start >= heap[0][0]:
                maxProfit = max(maxProfit, heap[0][1])
                heappop(heap)
            combinedJob = (end, maxProfit + profit)
            heappush(heap, combinedJob)
            
        while heap:
            maxProfit = max(maxProfit, heap[0][1])
            heappop(heap)
            
        return maxProfit
    
# Example usage:
# startTime = [1, 2, 3, 3]
# endTime = [3, 4, 5, 6]
# profit = [50, 10, 40, 70]
# solution = Solution()
# print(solution.jobScheduling(startTime, endTime, profit))