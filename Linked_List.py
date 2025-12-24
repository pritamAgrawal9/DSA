# Create a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a=Node(3)
b=Node(5)
c=Node(7)
a.next = b
b.next = c
head = a
#
# # Traverse
def printLL(head):
    curr = head
    while curr != None:
        print(curr.data, end=" ")
        curr = curr.next
#
# # Insertion
# 1. At the start
newNode = Node(2)
newNode.next = head
head = newNode

# # 2. Insert at Last
newNode1= Node(8)
curr1 = head
while curr1.next != None:
    curr1 = curr1.next

curr1.next = newNode1
# printLL(head)

# 3. Insert at a given index
ind = 3
d = Node(6)
curr = head
# for i in range(ind-1):
#     curr = curr.next
# d.next = curr.next
# curr.next = d
printLL(head)
print()
for i in range(ind-1): # i = 0 1 2
    # print(curr.data, end=" ")
    curr=curr.next
# print()
d.next = curr.next
curr.next = d
printLL(head)
