from functools import reduce # https://docs.python.org/3/library/functools.html

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        hash_dic = {c: i for i,c in enumerate('abcdefghij')}
        #print(hash_dic)
        numeric_total = lambda w: reduce(lambda s, c: 10*s + hash_dic[c], w, 0)
        #print(numeric_total(firstWord))
        return numeric_total(firstWord) + numeric_total(secondWord) == numeric_total(targetWord)

def main():
    firstWord = "acb"
    secondWord= "cba"
    targetWord = "cdb"
    s=Solution()
    print(s.isSumEqual(firstWord, secondWord, targetWord))
    firstWord = "aaa"
    secondWord= "a"
    targetWord = "aab"
    print(s.isSumEqual(firstWord, secondWord, targetWord))
    firstWord = "j"
    secondWord= "j"
    targetWord = "bi"
    print(s.isSumEqual(firstWord, secondWord, targetWord))

if __name__ == '__main__':
    main()
