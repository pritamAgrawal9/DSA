from collections import deque
class Binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __repr__(self):
        return f"Binary Tree ({self.data})"
root = Binary_tree(1)
root.left = Binary_tree(2)
root.right = Binary_tree(3)
root.left.left =Binary_tree(4)
root.left.right =Binary_tree(5)
def pre(node):
    if node:
        print(node.data)
        pre(node.left)
        pre(node.right)
pre(root)
from collections import deque

def level_order(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
level_order(root)  # Output: 1 2 3 4 5
