class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # neetcode solution, post order recursive dfs

        # Step 0: Put all unique letters into the adjacency list
        adj = { ch: set() for word in words for ch in word}

        # Step 1: Find all edges and put them in reverse adjacency list
        for word1, word2 in zip(words, words[1:]):
            for ch1, ch2 in zip(word1, word2):
                if ch1 != ch2:
                    adj[ch1].add(ch2)
                    break
            else: # if second word is prefix of first, then there is no solution, eg. w1 = apes, w2 = ape
                if len(word1) > len(word2):
                    return ""

        # Step 2: Recursive Depth First search
        output = []

        # Visited -> False, Current path -> True
        visit = {} # dictionary (key - ch, value - True/False)

        def dfs(c):
            if c in visit:
                return visit[c]

            visit[c] = True
            # visit all edges in adj list
            for nei in adj[c]:
                if dfs(nei):
                    return True
                # detect cycle, return True in DFS

            visit[c] = False
            output.append(c)
            return False

        # Step 3: Visit all nodes in adj list
        for c in adj:
            if dfs(c):
                return ''

        # Step 4: Post order DFS, reverse output and join into a string
        output.reverse()
        return ''.join(output)

        
