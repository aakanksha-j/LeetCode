class Solution:
    def twoSum(self, numbers, target):
        n=len(numbers)
        i=0
        j=n-1
        while i<j:
            s=numbers[i]+numbers[j]
            if s==target:
                return i+1,j+1
            elif s<target:
                i+=1
            else:
                j-=1

numbers = [3,24,50,79,88,150,345]
target = 200
s=Solution()
print(s.twoSum(numbers,target))
