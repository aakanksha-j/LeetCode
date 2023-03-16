class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # using math formula, refer diagrams by leetcode course solution
        # runtime O(n) for count method etc.
        # space O(1) for frequencies list which is constant for 26 letters
        
        if n == 0:
            return len(tasks)
        
        frequencies = [0]*26
        
        for task in tasks:
            frequencies[ord(task) - ord('A')] += 1
        
        f_max = max(frequencies)
        n_max = frequencies.count(f_max)
        
        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
        