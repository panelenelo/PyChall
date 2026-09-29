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
    # i = linkl.head
    # pos = i.next

    # while(i.next != None):
    #     prev = i
    #     i = pos
    #     if(i.next != None):
    #         pos = i.next
    #         i.next = prev
    #     else:
    #         i.next = prev
    #         linkl.head.next = None
    #         linkl.head = i
    #         break
    i, prev = linkl.head, None
    while(i != None):
        j = i.next
        i.next = prev
        prev = i
        i = j
    linkl.head = prev


def recursive_linked_list_reversal(list: SinglyLinkedList):
    new_head = recursive_aux(list.head, None)
    list.head=new_head


def recursive_aux(node: Node, prev: Node):
    j = node.next
    node.next = prev
    prev = node
    node = j
    if(node == None):
        return prev
    head = recursive_aux(node, prev)
    return head    




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
    #in_place_linked_list_reversal(list)
    recursive_linked_list_reversal(list)
    print("-")
    list.elPrint()



    
    

    









if __name__ == "__main__":
    main()