from __future__ import annotations  # For the Node reference inside the init function

from icecream import ic
from collections import deque


def linked_list_reversal_i(linkl: deque) -> deque:
    list = []
    for i in linkl:
        list.append(i)

    linkl.clear()
    m = len(list)-1
    while(m >= 0):
        linkl.append(list[m])
        m-=1
    return linkl

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
        

def in_place_linked_list_reversal(linkl: SinglyLinkedList):
    i = linkl.head
    j = i.next

    while(i.next != None):
        k = i
        i = j
        if(i.next != None):
            j = i.next
            i.next = k
        else:
            i.next = k
            linkl.head.next = None
            linkl.head = i
            break



def main():
    linkl = deque()
    linkl.append(1)
    linkl.append(2)
    linkl.append(4)
    linkl.append(7)
    linkl.append(3)
    linked_list_reversal_i(linkl)
    # ic(linkl)

    one = Node(1)
    list = SinglyLinkedList(one)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.elPrint()
    in_place_linked_list_reversal(list)
    print("-")
    list.elPrint()



    
    

    









if __name__ == "__main__":
    main()