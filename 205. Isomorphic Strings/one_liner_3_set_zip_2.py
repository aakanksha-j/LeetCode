class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # one line solution provided in comments in solution tab

        # time: O(N) - traverse strings twice for own set and zip set
        # space: O(N) - extra space for sets

        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

        # print(set(zip(s,t)))
        # s: "eggppspptp"
        # t: "addooroouo"
        # {('s', 'r'), ('t', 'u'), ('g', 'd'), ('p', 'o'), ('e', 'a')}
