class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Inspired from 205 Isomorphic strings one line solution provided in comments

        Example:
        s: "eggppspptp",
        t: "addooroouo"

        count - {'e': 1, 'g': 2, 'p': 5, 's': 1, 't': 1}
                {'a': 1, 'd': 2, 'o': 5, 'r': 1, 'u': 1}

        set(s) = {'e', 'g', 'p', 's', 't'}
        set(t) = {'a', 'd', 'o', 'r', 'u'}
        zip(s,t) = { ('e', 'a'), ('g', 'd'), ('p', 'o'), ('s', 'r'), ('t', 'u')}

        time: O(n * k) - n is len(words), k is len(word)
        space: O(n * k) - space for 3 sets - set(pattern), set(word), set(zip(pattern, word))

        isomorphic strings solution is return len(set(s)) == len(set(t)) == len(set(zip(s,t))) # true or false

        here, instead of comparing two strings, we are comparing one pattern to a list of strings, so solution is:
        """

        output = []
        for word in words:
            if len(set(pattern)) == len(set(word)) == len(set(zip(pattern, word))):
                output.append(word)

        return output
