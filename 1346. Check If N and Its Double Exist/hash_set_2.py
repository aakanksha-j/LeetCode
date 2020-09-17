class Solution:
    """Runtime:64 ms
       Memory: 13.8 MB
       Time complexity: n-square"""
    def checkIfExist(self, arr):
        seen=set()
        for i in arr:
            if i*2 in seen or i%2==0 and i//2 in seen:
                    return True
            seen.add(i)
        return False

def main():
    numbers =[1,3]
    s=Solution()
    print(s.checkIfExist(numbers))

if __name__ == '__main__':
    main()

# set is used instead of list because except hash collision condition
# it provides O(1) time complexity for 'in'.
