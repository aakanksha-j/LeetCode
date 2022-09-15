""" Coding question for Amazon SDE-2 - 2

You are given an array of length n. Each element in the index i refers to the
numberofProducts of the type i. You have to pick products from an subarray of
that array in such a way that the number of product picked from i should be
strictly less than the number of number of products picked from i+1.
Find the maximum number of products that can be picked.

Input
[7, 4, 5, 2, 6, 5]

Output
12

Explanation

1. Choose subarray (1,3) and pick products [3,4,5 ] . Note we pick only 3 from 1st index as 2nd index has only 4 products and we must pick elements stricly less in ith index than from an i+1th index. Total picked - 12
2. Choose subarray (3,6) and pick products [1,2,4,5]. Total picked - 9
3. Choose subarray (1,1) and pick all 7 products.

Input
6
2 9 4 7 5 2

Output
16

Explanation

In (1,2) subarray pick [ 2, 9]. Total Products - 11
In (1,4) subarray pick [2, 3, 4, 7] . Total Products - 16
In (1,5) subarray pick [1,2,3,4,5] . Total Products - 15 """

# in reverse order, take every index's max value
# iterate over list in reverse order picking up min(that index's value, previous
# value - 1), compare if max(current sum, overall_sum), after iterating over the
# entire array, return overall_sum.

# time: O(n^2), will have to iterate entire array (n)
#               and also inside while loop (n)
# space: O(1), no extra space

def numberofProducts(products):
    overall_sum = 0
    for i in range(len(products) - 1, -1, -1):
        cur_sum = products[i]
        j = i - 1
        cur_value = min(products[i] - 1, products[j])
        while j > -1 and cur_value > 0:
            cur_sum += cur_value
            cur_value = min(products[j - 1], cur_value - 1)
            j -= 1
        overall_sum = max(overall_sum, cur_sum)
    return overall_sum

products = [2, 9, 4, 7, 5, 2]
print(numberofProducts(products))
products = [7, 4, 5, 2, 6, 5]
print(numberofProducts(products))
products = [5,5,5,5]
print(numberofProducts(products))
