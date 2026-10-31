from __future__ import annotations  # For the Node reference inside the init function

class Node:
    def __init__(self, v: int, next: Node|None=None):
        self.v = v
        self.next = None

class SinglyLinkedList:
    def __init__(self, head: Node):
        self.head = head

    def append(self, v: int):
        n = Node(v, None)
        i = self.head
        while(i.next != None):
            i = i.next
        i.next = n

    def elPrint(self):
        i = self.head
        while(i != None):
            print(i.v)
            i = i.next
    
    def __iter__(self):
        self.a = self.head
        return self
    
    def __next__(self):
        if(self.a.next != None):
            self.a = self.a.next
            return self.a
        else:
            raise StopIteration
