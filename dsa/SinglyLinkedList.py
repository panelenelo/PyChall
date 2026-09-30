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
        