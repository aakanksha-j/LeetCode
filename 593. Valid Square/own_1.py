class Solution:
    """Approach 1: Find all 6 distances (4 sides and 2 diagonals). Maintain
                   a count for them. If criteria is satisfied then points form
                   a square.
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 24 ms
       Memory: 14.2 MB"""
    def validSquare(self, p1, p2, p3, p4):

        # measure distances between two points
        d12 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        if d12 == 0: return False
        d23 = (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2
        if d23 == 0: return False
        d34 = (p3[0]-p4[0])**2 + (p3[1]-p4[1])**2
        if d34 == 0: return False
        d41 = (p4[0]-p1[0])**2 + (p4[1]-p1[1])**2
        if d41 == 0: return False
        d42 = (p4[0]-p2[0])**2 + (p4[1]-p2[1])**2
        if d42 == 0: return False
        d31 = (p3[0]-p1[0])**2 + (p3[1]-p1[1])**2
        if d31 == 0: return False

        if d12 == d23:
            if d23 == d34 == d41 and d42 == d31:
                return True
        if d12 == 2 * d23:
            if d34 == d12 and d23 == d41 == d42 == d31:
                return True
        if d23 == 2 * d12:
            if d23 == d41 and d12 == d34 == d42 == d31:
                return True
        return False

def main():
    p1 = [0,0]
    p2 = [0,1]
    p3 = [1,1]
    p4 = [1,0]
    s=Solution()
    #print(s.validSquare(p1, p2, p3, p4))
    p1 = [0,0]
    p2 = [1,1]
    p3 = [0,1]
    p4 = [1,0]
    #print(s.validSquare(p1, p2, p3, p4))
    p1 = [0,0]
    p2 = [0,1]
    p3 = [1,0]
    p4 = [1,1]
    #print(s.validSquare(p1, p2, p3, p4))
    p1 = [0,-5]
    p2 = [0,5]
    p3 = [5,0]
    p4 = [-5,0]
    print(s.validSquare(p1, p2, p3, p4))


if __name__ == '__main__':
    main()
