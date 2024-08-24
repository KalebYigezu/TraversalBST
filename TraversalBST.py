#InOrder
class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data, end=" ")
        printInorder(root.right)

# Driver code
if __name__ == "__main__":
    # Build the tree
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    # Function call
    print("Inorder Traversal:", end=" ")
    printInorder(root)

#PreOrder-----------------------------------------------------------------------
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPreOrder(node):
    if node is None:
        return
    print(node.data, end = " ")
    printPreOrder(node.left)
    printPreOrder(node.right)

if __name__ == "__main__":
    # Build the tree
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Preorder Traversal: ", end = "")
    printPreOrder(root)
#PostOrder-------------------------------------------------------------
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def printPostOrder(node):
    if node is None:
        return

    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data, end=" ")


if __name__ == "__main__":
    root = Node(100)
    root.left = Node(20)
    root.right = Node(200)
    root.left.left = Node(10)
    root.left.right = Node(30)
    root.right.left = Node(150)
    root.right.right = Node(300)

    print("Postorder Traversal: ", end="")
    printPostOrder(root)
  
