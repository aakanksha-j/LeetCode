class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashmap = {}
        count_change = 0
        for width, height in rectangles:
            prev = hashmap.get((width / height), 0)
            count_change += prev
            hashmap[(width / height)] = prev + 1
        return count_change

# similar to 1814 Count nice pairs, 2364 Count bad pairs

time O(N) for going through n nodes
space O(N) for hashmap

9 9 2022 2001 Number of Pairs of Interchangeable Rectangles
