class Solution:
    """Approach 1: Use dictionary to count and compare. Solution works for
                   unicode characters as well.
       Time complexity: O(n)
       Space complexity: O(n) for dictionary
       Runtime: 52 ms
       Memory: 14.4 MB"""
    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        com_dic={}
        for ch in s:
            com_dic[ch]=com_dic.get(ch,0)+1
        for ch in t:
            com_dic[ch]=com_dic.get(ch,0)-1
        for ch in com_dic:
            if com_dic[ch]!=0:
                return False
        return True

def main():
    p='heart'
    t='earth'
    s=Solution()
    print(s.isAnagram(p,t))
    p ='ra#'
    t ='#ar'
    print(s.isAnagram(p,t))

if __name__ == '__main__':
    main()
