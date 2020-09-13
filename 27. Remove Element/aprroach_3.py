class Solution:
    def removeElement(self, nums, val):
        i=0
        z=len(nums)-1
        while i<=z:
            if nums[i]==val:
                if nums[z]!=val:
                    nums[i],nums[z]=nums[z],nums[i]
                    z-=1
                    i+=1
                else:
                    z-=1
            else:
                i+=1
        return i

def main():
    numbers = [2,2]
    target = 2
    s=Solution()
    print(s.removeElement(numbers,target))
    print(numbers)

if __name__ == '__main__':
    main()
