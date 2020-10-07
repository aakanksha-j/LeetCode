class Solution:
    """Approach 2: Use a dictionary to store count and return element with
                   count 1.
       Time complexity: O(n)
       Space complexity: O(n) for dictionary.
       Runtime: 84 ms
       Memory: 16.4 MB"""
    def singleNumber(self, nums):
        num_dic={}
        for n in nums:
            num_dic[n]=num_dic.get(n,0)+1
        for n in nums:
            if num_dic[n]==1:
                return n

def main():
    numbers =[2,1,2]
    s=Solution()
    print(s.singleNumber(numbers))
    numbers =[4,1,2,1,2]
    print(s.singleNumber(numbers))

if __name__ == '__main__':
    main()
