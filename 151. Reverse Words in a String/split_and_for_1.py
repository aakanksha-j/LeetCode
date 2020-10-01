class Solution:
    """Approach 1: Use split to get a list of words and then traverse the list
                   to add last word first.
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 20 ms
       Memory: 14.4 MB"""
    def reverseWords(self, s):
        sa=s.split()
        s=''
        for i in range(len(sa)):
            if i==0:
                s+=sa[-(i+1)]
            else:
                s+=' '+sa[-(i+1)]
        return s

def main():
    p=Solution()
    s='hello world'
    print(p.reverseWords(s))

if __name__ == '__main__':
    main()
