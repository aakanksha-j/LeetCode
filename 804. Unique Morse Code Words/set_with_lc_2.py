class Solution:
    """Approach 1: Use a dictionary to store morse code and use 3 for loops,
                   one for reading words, one for every character in word and
                   one for adding unique patterns to list.
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 32 ms
       Memory: 14.3 MB
    """
    def uniqueMorseRepresentations(self, words) -> int:
        morse_code_list = [".-","-...","-.-.","-..",".","..-.","--.","....",
                           "..",".---","-.-",".-..","--","-.","---",".--.",
                           "--.-",".-.","...","-","..-","...-",".--","-..-",
                           "-.--","--.."]
        seen = {''.join(morse_code_list[ord(ch) - ord('a')] for ch in word)
                for word in words} # curly brackets without key value pairs: set
        #print(seen)
        return len(seen)

def main():
    words = ["gin", "zen", "gig", "msg"]
    s=Solution()
    print(s.uniqueMorseRepresentations(words))
    words =['abcdefghijkl', 'mnopqrstuvwx']
    print(s.uniqueMorseRepresentations(words))
    words =['mnopqrstuvwx', 'mnopqrstuvwx']
    print(s.uniqueMorseRepresentations(words))
    words =['yz', 'yz']
    print(s.uniqueMorseRepresentations(words))

if __name__ == '__main__':
    main()
