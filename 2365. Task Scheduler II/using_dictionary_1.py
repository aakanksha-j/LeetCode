"""
You are given a 0-indexed array of positive integers tasks, representing tasks that need to be completed in order, where tasks[i] represents the type of the ith task.

You are also given a positive integer space, which represents the minimum number of days that must pass after the completion of a task before another task of the same type can be performed.

Each day, until all tasks have been completed, you must either:

Complete the next task from tasks, or
Take a break.
Return the minimum number of days needed to complete all tasks.

Example 1:

Input: tasks = [1,2,1,2,3,1], space = 3
Output: 9
Explanation:
One way to complete all tasks in 9 days is as follows:
Day 1: Complete the 0th task.
Day 2: Complete the 1st task.
Day 3: Take a break.
Day 4: Take a break.
Day 5: Complete the 2nd task.
Day 6: Complete the 3rd task.
Day 7: Take a break.
Day 8: Complete the 4th task.
Day 9: Complete the 5th task.
It can be shown that the tasks cannot be completed in less than 9 days.
"""
class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        output = 0
        dictionary_task_position = {}
        for task in tasks:
            if task not in dictionary_task_position:
                dictionary_task_position[task] = output = output + 1
            else:
                dictionary_task_position[task] = output = max(output, dictionary_task_position[task] + space) + 1
        return output
    


# runtime O(n)
# space O(n) for dictionary