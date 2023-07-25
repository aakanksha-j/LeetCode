"""Given a binary tree represented as an array, for example, [3,6,2,9,-1,10] represents a binary tree and -1 is a non existent node. Write a function that determines whether the left or right branch of the ree is larger. The size of each branch s the sum of the node values. The function should return the string "Right" if the right size is larger and "Left" if the left size is larger. If the tree has 0 nodes of it the size of the branches are equal, return the empty string.
function public String findLargeTree(long[] arr)
Sample cases:

1 [3,6,2,9,-1,10] return "Left".
[1,10,5,1,0,6] return ""

Explanation: Size of both branches are equal
My comments:
From the pictoral representation of the tree, I could determine that the array is a representation of the level order traversal of the tree. So given input array arr, arr[0] is the root.
I came up with a simple solution using 2 loops where given root index p, 2*p+1 are the left children and 2*p + 2 are the right children. I updated p each time I found a index that satisfied the criteria.
I didn't give it my best shot because I was thrown off my game by this kind of representation. having solved so many LC tree problems with TreeNode class and LC problems that require you to construct b-trees usually have 2 traversal lists (iorder/preorder/postorder) so the difficulty level was a bit higher.
But I think the best way to approach this is to go through the trouble of constructing a binary tree and then finding the sum of the left and right subtrees. I wanted to know the thoughts of LC community on this.

binary tree
path sum
similar to 894 All possible full binary trees recursive solution"""


def solution(arr):
    # Type your solution here 
    if not arr: return ""
    
    left_sum = tree_sum(arr,1)
    right_sum = tree_sum(arr,2)
    
    if left_sum == right_sum: return ""
    return "Left" if left_sum > right_sum else "Right"
    
def tree_sum(arr,i):
    if len(arr)<=i or arr[i]==-1: return 0
    return arr[i] + tree_sum(arr, 2*i+1) + tree_sum(arr, 2*i+2)
    pass
