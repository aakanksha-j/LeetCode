class Solution:
    def maxArea(self, height: List[int]) -> int:
        # leetcode solution - two pointers approach
        
        # time: O(N) - single pass
        # space: O(1) - constant space is used
        
        l, r = 0, len(height) - 1
        output = 0
        
        while l < r:
            #print(l, r)
            amount_of_water = (r - l) * min(height[l], height[r])
            #print(amount_of_water)
            output = max(amount_of_water, output)
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
                    
        return output
            
                
                    
# solution similar to trapping rain water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        output = 0
        
        while l < r:
            if max_l <= max_r:
                if max_l >= height[l]:
                    amount_of_water = (r - l) * min(max_l, max_r)
                    output = max(amount_of_water, output)
                    l += 1
                else:
                    max_l = height[l]
            else:
                if max_r >= height[r]:
                    amount_of_water = (r - l) * min(max_l, max_r)
                    output = max(amount_of_water, output)
                    r -= 1
                else:
                    max_r = height[r]
                    
        return output
            
                
                    
# always move the pointer which is smaller in value as we want to get max area 
# which depends on width (r-l) and min(max_l, max_r) 