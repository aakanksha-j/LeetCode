class Solution:
    """Approach 1:
       Time complexity: O(1)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14.2 MB"""
    def validSquare(self, p1, p2, p3, p4):
        ((x1, y1), (x2, y2), (x3, y3), (x4, y4)) = sorted([p1, p2, p3, p4])

        if x1 == x4:
            return False

        if x2 - x1 != x4 - x3:
            return False

        if y2 - y1 != y4 - y3:
            return False

        if x2 - x1 != abs(y3 - y1):
            return False

        if x3 - x1 != abs(y2 - y1):
            return False

        if (y2 - y1) * (y1 - y3) < 0:
            return False

        return True

def main():
    p1 = [0,0]
    p2 = [0,1]
    p3 = [1,1]
    p4 = [1,0]
    s=Solution()
    print(s.validSquare(p1, p2, p3, p4))
    p1 = [0,-5]
    p2 = [0,5]
    p3 = [5,0]
    p4 = [-5,0]
    print(s.validSquare(p1, p2, p3, p4))

if __name__ == '__main__':
    main()
