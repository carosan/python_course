#Calculate the sum of the values in a binary tree

class Node:
    left = None
    right = None
    v = 0

#define a function to calculate the sum of the values in a tree. 
#It receives the root of a tree and returns the sum of the values in the tree
def calculate_sum(root):
    if root is None:
        return 0
    return root.v+calculate_sum(root.left)+calculate_sum(root.right)
  
n1 = Node()
n1.v = 1
  
n3 = Node()
n3.v = 3

n4 = Node()
n4.v = 4
n4.right = n1

n2 = Node()
n2.v = 2
n2.left = n3
n2.right = n4

print calculate_sum(n2)