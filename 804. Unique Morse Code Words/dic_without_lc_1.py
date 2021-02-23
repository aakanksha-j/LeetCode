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
        dict = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".",'f':"..-.",
                'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..",
                'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.",
                's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-",
                'y':"-.--",'z':"--.."}
        patterns = []

        for word in words:
            morse_code = ''
            for ch in word:
                morse_code = morse_code + dict[ch]
            if not patterns:
                patterns.append(morse_code)
                continue
            else:
                flag = True
                for pattern in patterns:
                    if pattern == morse_code:
                        flag = False
                        break
                if flag:
                    patterns.append(morse_code)

        return len(patterns)

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
