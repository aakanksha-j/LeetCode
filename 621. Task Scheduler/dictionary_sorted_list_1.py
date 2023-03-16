"""Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks."""

# edge case: 
# ["A","A","A","A","B","B","B","B","C","C","C","C","D","D","D","D","E","F"]
# n = 4
# output = 18, expected = 19

# own solution
# needs dictionary of f
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        print(len(tasks))
        if n == 0:
            return len(tasks)
        
        # create a dictionary of tasks as key and frequency as values
        task_frequency_map = {}
        for task in tasks:
            task_frequency_map[task] = task_frequency_map.get(task, 0) + 1
            
        # sort dictionary by value
        sorted_list = sorted(task_frequency_map.items(), key = lambda x: x[1], reverse = True)
        
        max_frequency = sorted_list[0][1]
        
        gap_between_two_same = max_frequency - 1
        idle_time = n * gap_between_two_same
         
        # # idle time not needed
        # if len(tasks) > max_frequency + idle_time:
        #     return len(tasks)
        
        # reduce idle_time by filling it with other tasks
        for task, frequency in sorted_list[1:]:
            minimum_of_three = min(gap_between_two_same, frequency, idle_time)
            frequency -= minimum_of_three
            idle_time -= minimum_of_three
            if idle_time == 0:
                break
        
        total_output = max_frequency + idle_time
    
        for task, frequency in sorted_list[1:]:
            total_output += frequency
            
        return total_output
        