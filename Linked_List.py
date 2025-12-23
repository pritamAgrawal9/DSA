class Node:
    def __init__(self,data):
        self.data = data
        self.node = None
a=Node(3)
b=Node(5)
c=Node(7)
a.next = b
b.next = c
head = a
