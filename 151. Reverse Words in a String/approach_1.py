class Solution:
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
