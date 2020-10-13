class Solution:
    """Approach 1: Traverse array backwards
       Time complexity: O(n)
       Space complexity: O(1)
       Runtime: 116 ms
       Memory: 15.3 MB
    """
    def replaceElements(self, arr):
        if len(arr)<1:
            return
        if len(arr)==1:
            return [-1]
        for i in range(len(arr)-1,-1,-1):
            if i == len(arr) - 1:
                highest = arr[i]
                arr[i] = -1
            else:
                if arr[i] > highest:
                    arr[i], highest = highest, arr[i]
                else:
                    arr[i] = highest
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
