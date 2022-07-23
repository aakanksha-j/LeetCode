class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # leetcode solution - merge sort

        # if number in left array is smaller than number in right array, we will shift it j-mid times

        # time: O(N.logN) for merge sort
        # space: O(N) extra space for arr, temp with value and index

        n = len(nums)
        arr = [[v, i] for i, v in enumerate(nums)] # record value and index
        result = [0] * n

        def merge(arr, left, right, mid):
            # merge [left, mid) and [mid, right)

            i, j = left, mid
            temp = [] # use temp to temporarily store sorted array

            while i < mid and j < right:
                if arr[i][0] <= arr[j][0]:
                    # j - mid numbers jump to the left side of arr[i]
                    result[arr[i][1]] += j - mid
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            # when one of the subarrays is empty
            while i < mid:
                # j - mid numbers jump to the left of arr[i]
                result[arr[i][1]] += j - mid
                temp.append(arr[i])
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1

            # restore from temp
            for i in range(left, right):
                arr[i] = temp[i - left]

        def merge_sort(arr, left, right):
            #[left, right) means right not included
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid, right)
            merge(arr, left, right, mid)

        merge_sort(arr, 0, n)

        return result

        # testcase: [7,2,5,4,1,6] --> [7,2,5] [4,1,6] index of 5(i=2) and index of 6(j=5) mid is 3 so result[index of 5 i.e 2] = j - mid = 5 - 3 += 2
        
