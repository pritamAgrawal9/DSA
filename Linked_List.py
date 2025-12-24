# Create a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class DoublyNode:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
# a=Node(3)
# b=Node(5)
# c=Node(7)
# a.next = b
# b.next = c
# c.next=a
# head = a
#
# # Traverse
# def printLL(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=" ")
#         curr = curr.next
#
# # Insertion
# 1. At the start
# newNode = Node(2)
# newNode.next = head
# head = newNode

# # 2. Insert at Last
# newNode1= Node(8)
# curr1 = head
# while curr1.next != None:
#     curr1 = curr1.next
#
# curr1.next = newNode1
# printLL(head)

# 3. Insert at a given index
# ind = 3
# d = Node(6)
# curr = head
# for i in range(ind-1):
#     curr = curr.next
# d.next = curr.next
# curr.next = d
# printLL(head)
# print()
# for i in range(ind-1): # i = 0 1 2
#     # print(curr.data, end=" ")
#     curr=curr.next
# print()
# d.next = curr.next
# curr.next = d
# printLL(head)
# print()
# Deletion in linked list
# 1. deletion of head
# head = head.next

# 2. deletion of last node
# curr2 = head
# while curr2.next.next!=None:
#     curr2 = curr2.next
# curr2.next = None
# printLL(head)

# 3. deletion of node at a given index
# for j in range(ind-1):
#     curr2 = curr2.next
# curr2.next = curr2.next.next
# printLL(head)

# Circular linked list
a=Node(3)
b=Node(5)
c=Node(7)
a.next = b
b.next = c
c.next=a
head = a
curr=head
while True:
    print(curr.data,end=' ')
    curr = curr.next
    if curr == head:
        break
