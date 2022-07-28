class Solution:
    """Approach 2: Use .count() and set function.
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 32 ms
       Memory: 14.3 MB"""
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        elif s==t:
            return True
        else:
            check_s=set(s)
            check_t=set(t)
            if check_s==check_t:
                for ch in check_s:
                    if s.count(ch)!=t.count(ch):
                        return False
                return True
            else:
                return False

def main():
    p='heart'
    t='earth'
    s=Solution()
    print(s.isAnagram(p,t))
    p ='#at'
    t ='ta#'
    print(s.isAnagram(p,t))

if __name__ == '__main__':
    main()
