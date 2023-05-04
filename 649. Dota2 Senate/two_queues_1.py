"""
649. Dota2 Senate
Medium

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

 

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.
Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation: 
The first senator comes from Radiant and he can just ban the next senator's right in round 1. 
And the second senator can't exercise any rights anymore since his right has been banned. 
And the third senator comes from Dire and he can ban the first senator's right in round 1. 
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.
 

Constraints:

n == senate.length
1 <= n <= 104
senate[i] is either 'R' or 'D'."""

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        r_q = [i for i, party in enumerate(senate) if party == 'R']
        d_q = [i for i, party in enumerate(senate) if party == 'D']
        
        r_q = deque(r_q)
        d_q = deque(d_q)
        
        #print(r_q, d_q)
        while r_q and d_q:
            if r_q[0] < d_q[0]:
                d_q.popleft()
                r_q.append(r_q.popleft() + n)
            else:
                r_q.popleft()
                d_q.append(d_q.popleft() + n)
        
        return 'Radiant' if r_q else 'Dire'
    
# time O(n) - populating queue, length of string, no of senators
# space O(n) - for storing senator indices in queue
# https://leetcode.com/problems/dota2-senate/discuss/1704597/C%2B%2B-Explanation-with-Diagram
# Greedy approach - ban the nearest opponent 
# how many rounds can we have? log2 N
# how many votes can we have? N
# first round, N senators; second round, N/2 senators ....
# therefore, first round, N/2 votes, second round, N/4 votes...
# N/2 + N/4 + N/8 .. summation = geometric progression = (N/2).(1/(1-1/2)) = N