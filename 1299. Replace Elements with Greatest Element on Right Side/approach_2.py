class Solution:
    """Approach 1: Traverse array backwards
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 116 ms
       Memory: 15.2 MB
    """
    def replaceElements(self, arr):
        N = len(arr)
        greatest = -1
        for i in range(N-1, -1, -1):
            origin = arr[i]
            arr[i] = greatest
            if origin > greatest:
                greatest = origin
        return arr

def main():
    numbers = [17,18,5,4,6,1]
    s=Solution()
    print(s.replaceElements(numbers))
    numbers = [16,17,18]
    print(s.replaceElements(numbers))
    numbers = [18,17,16]
    print(s.replaceElements(numbers))
    numbers = [17,16]
    print(s.replaceElements(numbers))
    numbers = [15,16]
    print(s.replaceElements(numbers))
    numbers = [16]
    print(s.replaceElements(numbers))


if __name__ == '__main__':
    main()
