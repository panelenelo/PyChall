from SinglyLinkedList import SinglyLinkedList, Node
from icecream import ic


def remove_node(list: SinglyLinkedList, n: int) -> Node:
    current = list.head
    kth = current
    count = 0
    while(current.next):
        if(count == n+1):
            kth = kth.next
            current = current.next
        else:
            count += 1
            current = current.next
    kth.next = kth.next.next
    return list.head


def main():
    one = Node(1)
    list = SinglyLinkedList(one)
    list.append(2)
    list.append(3)
    list.append(4)
    list.append(5)
    list.elPrint()
    print("-")
    remove_node(list, 2)
    list.elPrint()


if __name__ == "__main__":
    main()