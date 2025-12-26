# implementing stack through list
st=[]
# st.append(8)
# st.append(1)
# st.append(2)
# print(st.pop(-1))
# print("top " + str(st[-1]))

# Implementation through class
# class Stack:
#     def __init__(self):
#         self.st = []
#     def push(self,i):
#         self.st.append(i)
#
#     def pop(self):
#         if len(self.st) == 0:
#             return
#         x = self.st[-1]
#         self.st.pop()
#         return x
#
#     def top(self):
#         if len(self.st) == 0:
#             return
#         return self.st[-1]
#     def size(self):
#         return len(self.st)
# op = Stack()
# op.push(1)
# op.push(2)
# op.push(3)
# print(op.pop())

# Implementing stack using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, x):
        if self.top is None:
            self.top = Node(x)
        else:
            n = Node(x)
            n.next = self.top
            self.top = n
        self.length += 1
    def pop(self):
        if self.top is None:
            return
        else:
            x = self.top.data
            self.top = self.top.next
        self.length -= 1
        return x

    def get_top(self):
        if self.top is None:
            return
        else:
            return self.top.data

op = Stack()
op.push(1)
op.push(2)
op.push(3)
print(op.length)
print(op.pop())
print(op.get_top)




