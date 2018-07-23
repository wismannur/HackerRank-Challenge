class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        if self.root is None :
            self.root = Node(val)
        else :
            self.insertNode(val, self.root)

    def insertNode(self, val, node) :
        if val < node.info :
            if node.left :
                self.insertNode(val, node.left)
            else :
                node.left = Node(val)
        elif val > node.info :
            if node.right :
                self.insertNode(val, node.right)
            else :
                node.right = Node(val)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

