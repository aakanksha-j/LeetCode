class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        """1. using sort
        # time: O(N log N) , space: O(1)
        nums.sort()
        return nums[len(nums) - k]

        2. Python's inbuilt function, returns list upto k elements,
        # time: O(nlogk)
        # space: O(k) to store k elements in list
        return heapq.nlargest(k, nums)[-1]
        """

        """3. neetcode and own's quicksort solution
        steps:
        1. select a random element between left and right as pivot index
        2. move element at pivot index to right
        3. move all smaller elements to left
        4. move pivot to its right place
        5. recursively repeat until k_smallest = pivot index"""

        k_smallest = len(nums) - k # kth largest element is (n-k)th smallest element in a sorted list, from 0.

        def quickselect(l, r):

            pivot_index = random.randint(l, r)

            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]

            i = l - 1 # index
            for j in range(l, r):
                if nums[j] <= nums[r]:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[r] = nums[r], nums[i + 1]

            # i+1 is the index to be returned by partition method as that is the
            # right place of current element.

            if i + 1 == k_smallest:
                return nums[i + 1]
            elif k_smallest < i + 1:
                return quickselect(l, i) # store_index - 1
            else:
                return quickselect(i + 2, r)

        return quickselect(0, len(nums) - 1) # store_index + 1


        """# quickselect algorithm

        def partition(A, l, r):
            # similar to quick sort algorithm

            i, j = l - 1, l
            for j in range(l, r):
                if A[j] <= A[r]:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i + 1], A[r] = A[r], A[i + 1]
            return i+1

        def select(l, r, k_smallest):

            pivot_index = partition(nums, l, r)

            if pivot_index == k_smallest:
                return nums[k_smallest]

            elif pivot_index < k_smallest:
                return select(pivot_index + 1, r, k_smallest)

            else:
                return select(l, pivot_index - 1, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)

        # leetcode solution
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # 1. move pivot to end
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1

            # 3. move pivot to its final place
            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def select(left, right, k_smallest):
            """
            #Returns the k-th smallest element of list within left..right
        """
            if left == right:       # If the list contains only one element,
                return nums[left]   # return that element

            # select a random pivot_index between
            pivot_index = random.randint(left, right)

            # find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return nums[k_smallest]
            # go left
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, k_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)"""
