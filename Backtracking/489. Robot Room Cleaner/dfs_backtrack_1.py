# test case: [[1,1,1],[1,1,1],[1,1,1]] , row = 1, col = 1

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell = (0, 0), dir = (-1, 0)):
            print(cell)
            # add
            visited.add(cell)
            robot.clean()

            r,c = cell
            for i in range(4):
                # clockwise: up (-1, 0), right (0, 1), down (1, 0), left (0, -1)
                x, y = dir
                new_cell = (r + x, c + y)
                
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, dir)
                    go_back() # backtrack to the previous cell
                robot.turnRight()

                dir = (-y, x) # rotate 90 degree so that robot explores new direction on same cell


        visited = set() # (r,c)

        backtrack()

# https://leetcode.com/problems/robot-room-cleaner/discuss/150132/Very-clear-Python-DFS-code-beat-99-%2B
# time: 4 directions per cell minus obstacles, 4. (N - M) - N is # of cells, M is # of obstacles
# space: N - M, visited set
