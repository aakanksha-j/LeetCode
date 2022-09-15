from math import comb

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return n
        sum=1
        no_of_2_steps=n//2 #maximum 2 steps possible for given no of stairs
        if n%2==0:
            j=no_of_2_steps
        else:
            j=no_of_2_steps+1
        for i in range(no_of_2_steps,0,-1):
            j_combination_i=comb(j,i)
            sum+=j_combination_i
            j+=1
        return sum

s=Solution()
print(s.climbStairs(9))


"""
def __init__(self):
    self.cache={0:1,1:1,2:2}

def cached_fac(self,number):
    #print('a:',number)
    if number in self.cache:
        #print('b:',self.cache[number])
        return self.cache[number]
    self.cache[number]=number*self.cache[number-1]
    return self.cache[number]"""
