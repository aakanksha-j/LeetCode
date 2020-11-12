class Solution:
    """Approach 1: Traverse every bit using single pointer. Flip and invert.
       Time complexity: O(n)
       Space complexity: O(n)
       Runtime: 48 ms
       Memory: 14.3 MB"""

    def flipAndInvertImage(self, A):
        if len(A)<0 or len(A)>20: return 'Invalid input.'
        for image in A:
            for i in range(len(image)):
                if image[i]>1 or image[i]<0: return 'Invalid input.'
        for image in A:
            for i in range(len(image)//2):
                # alternative 1: image[i], image[-(i+1)] = image[-(i+1)] ^ 1, image[i] ^ 1
                image[i], image[-(i+1)] = image[-(i+1)], image[i]
                image[i], image[-(i+1)] = self.__invert(image[i]), self.__invert(image[-(i+1)])
            if len(image)%2: # odd number of elements in row
                image[len(image)//2] = self.__invert(image[len(image)//2])
        return A

        #  alternative 2: return [[1-i for i in row[::-1]] for row in A]

    def __invert(self, bit):
        if bit == 0:
            bit = 1
        else:
            bit = 0
        return bit

def main():
    numbers = [[1,0,0],[1,1,1],[0,1,0]]
    s=Solution()
    print(s.flipAndInvertImage(numbers))
    numbers = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print(s.flipAndInvertImage(numbers))
    numbers = [[12]]
    print(s.flipAndInvertImage(numbers))

if __name__ == '__main__':
    main()
