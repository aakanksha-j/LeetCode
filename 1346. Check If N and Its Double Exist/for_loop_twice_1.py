class Solution:
    """Runtime:84 ms
       Memory: 13.9 MB
       Time complexity: n-square"""
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==2*arr[j] or arr[j]==2*arr[i]:
                    return True
        return False

def main():
    numbers =[-500,-1000]
    s=Solution()
    print(s.checkIfExist(numbers))

if __name__ == '__main__':
    main()
