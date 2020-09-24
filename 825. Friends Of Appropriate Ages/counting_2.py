class Solution:
    """Approach 2: Make a list of count based on ages. Go through two
                   nested count loops to calculate total friend requests
                   possible. Subtract friend requests sent to yourself.
       Time complexity: O(A2+n) = 1 age for loop + 2 count for loops
       Space complexity: O(A) = count array
       Runtime: 436 ms
       Memory: 14.5 MB"""
    def numFriendRequests(self, ages):
        count=[0]*121
        for age in ages:
            count[age]+=1
        ans=0
        for ageA,countA in enumerate(count):
            for ageB,countB in enumerate(count):
                if ageB<=0.5*ageA+7:continue
                if ageB>ageA:continue
                ans+=countA*countB
                if ageA==ageB: ans-=countA
        return ans

def main():
    numbers =[16,16,16]
    s=Solution()
    print(s.numFriendRequests(numbers))
    numbers =[16,17,18]
    print(s.numFriendRequests(numbers))
    numbers =[20,30,100,110,120]
    print(s.numFriendRequests(numbers))

if __name__ == '__main__':
    main()

# Expected output: 2,2,3
