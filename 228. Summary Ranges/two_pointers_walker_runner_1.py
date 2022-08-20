class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        walker = runner = 0
        while runner < len(nums):
            nums[walker] = nums[runner]
            output.append(str(nums[walker]))
            while runner + 1 < len(nums) and nums[runner + 1] == 1 + nums[runner]:
                runner += 1
            #print(runner, walker)
            if nums[runner] != nums[walker]:
                #print(output)
                output[walker] = (str(nums[walker]) + '->' + str(nums[runner]))
            runner += 1
            walker += 1
        return output
        
