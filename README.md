# Competitive-Coding-5

maxValueEachLevelofBinaryTree.py
This finds the max value among each level of a tree.

This is solved using the BFS algorithm. Where every element in the queue is added and takes max value in that resultant max. 
then max is appended to the result list.

Mistake Faced While coding:
use only pop() by using queue list without collections.queue import which used to take root.right elements always then would check with the root.left elements.

validSuduko.py 
is solved using the hash map to check the whether the number is repeated in each row, column and 3X3 matrix
