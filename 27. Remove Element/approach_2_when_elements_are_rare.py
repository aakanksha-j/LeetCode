class Solution:
    def removeElement(self, nums, val):
        i=0
        n=len(nums)
        while i<n:
            if nums[i]==val:
                nums[i]=nums[n-1] #swap
                n-=1 # reduce array size by one
            else:
                i+=1
        return n

def main():
    numbers = [0,1,2,2,3,0,4,2]
    target = 2
    s=Solution()
    print(s.removeElement(numbers,target))
    print(numbers)

if __name__ == '__main__':
    main()
