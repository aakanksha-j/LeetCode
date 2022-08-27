class Solution:
    def twoSum(self, numbers, target):
        dic={}
        for i,num in enumerate(numbers):
            if target-num in dic:
                return dic[target-num]+1,i+1
            dic[num]=i

numbers = [3,24,50,79,88,150,345]
target = 200
s=Solution()
print(s.twoSum(numbers,target))
