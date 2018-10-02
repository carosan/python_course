#calculate the hegiht of a binary tree 
#Define the Node class that contains two fields as the binary tree only have 2 branches
class Node:
    left = None
    right = None
    
#a function that returns the height of the binary tree
def height(root):
    if root is None:
        return -1
    return max(height(root.left), height(root.right)) + 1

n8 = Node()

n7 = Node()

n3 = Node()
n3.right = n8
n3.left = n7

n5 = Node()

n1 = Node()
n1.right = n5
n1.left = n3

print(height(n1))