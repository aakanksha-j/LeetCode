class FreqStack:
    # https://leetcode.com/problems/maximum-frequency-stack/discuss/163410/C%2B%2BJavaPython-O(1)
    
    # freq: Counter({5: 3, 7: 2, 4: 1})
    # m: defaultdict(<class 'list'>, {1: [5,7,4], 2: [5, 7], 3: [5]})
    
    # time: O(1) - to push and pop, go through every element twice
    # space: O(N) for dictionaries freq and m

    # if element val has n frequency, we will push val n times in m[1], m[2] .. m[n] 

    def __init__(self):
        self.freq = collections.Counter()
        self.m = collections.defaultdict(list)
        self.maxf = 0
        
    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxf = max(self.maxf, self.freq[val])
        self.m[self.freq[val]].append(val)
        #print(self.freq, self.m, self.maxf)

    def pop(self) -> int:
        #print(self.maxf)
        val = self.m[self.maxf].pop()
        if not self.m[self.maxf]: self.maxf -= 1
        self.freq[val] -= 1
        #print(self.freq, self.m, self.maxf)
        return val    


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()