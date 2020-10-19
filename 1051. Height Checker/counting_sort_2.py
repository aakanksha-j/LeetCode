"""https://leetcode.com/problems/height-checker/discuss/347368/Easy-Python-O(n)-Let's-step-through-the-algorithm"""
class Solution:
    """Approach 2: Used counting sort to get sorted array and then took sum of
                   mismatch between original and sorted array using a list
                   comprehension and zip.
                   The reason we choose counting sort is because constraints
                   mention that len(heights) and heights[i] both range between
                   1 to 100. Since counting sort is useful when k (max value in
                   array) and length of array are in similar range.
       Time complexity: O(n)
       Space complexity: O(n) for another array 'output'
       Runtime: 36 ms
       Memory: 13.9 MB"""
    def heightChecker(self, heights):
        k = max(heights) + 1
        C = [0] * k
        for number in heights:
            C[number] += 1
        for idx, n in enumerate(C[1:], 1):
            C[idx] = C[idx - 1] + n # take cumulative
        output = heights[:]
        for j in range(len(heights)-1, -1, -1):
            output[C[heights[j]] - 1] = heights[j]
            C[heights[j]] -= 1
        return sum(h1 != h2 for h1, h2 in zip(heights, output))

def main():
    numbers = [1,1,4,2,1,3] # 3
    s=Solution()
    print(s.heightChecker(numbers))
    numbers = [5,1,2,3,4] # 5
    print(s.heightChecker(numbers))
    numbers = [1,2,3,4,5] # 0
    print(s.heightChecker(numbers))
    numbers = [1,2,1,2,1,1,1,2,1] # 4
    print(s.heightChecker(numbers))

if __name__ == '__main__':
    main()
