from icecream import ic
from SinglyLinkedList import SinglyLinkedList, Node



def find_intersection(ll1: SinglyLinkedList, ll2: SinglyLinkedList) -> Node:
    # Traversing both lists
    #it1 = iter(ll1)
    #it2 = iter(ll2)
    #print("____---____")
    #ptr_a = it1
    #ptr_b = it2
    #while (ptr_a.a.v != ptr_b.a.v):
    #    ic(next(it1).v)
    #    ic(next(it2).v)
    #    print("******")
    ptr_a, ptr_b = ll1.head, ll2.head
    while (ptr_a.v != ptr_b.v):
        if(ptr_a.next == None):
            ptr_a.next = ll2.head
        if(ptr_b.next == None):
            ptr_b.next = ll1.head
        ptr_a = ptr_a.next
        ptr_b = ptr_b.next
    return ptr_a







def main():
    one = Node(1)
    ll1 = SinglyLinkedList(one)
    ll1.append(2)
    ll1.append(3)
    ll1.append(7)
    ll1.append(4)
    ll1.append(5)
    ll1.elPrint()
    print("-----")
    ll2 = SinglyLinkedList(Node(0))
    ll2.append(9)
    ll2.append(19)
    ll2.append(92)
    ll2.append(72)
    ll2.append(35)
    ll2.append(7)
    ll2.append(4)
    ll2.append(5)
    ll2.elPrint()
    
    intersection = find_intersection(ll1, ll2)
    print("---**---")
    print(intersection.v)

    

#y = 1-4-6-4-2-6-9-7-5-3-2-3-2-5-7
#x = 6-5-3-8-9-5-3-2-5-7

#yx= 1-4-6-4-2-6-9-7-5-3-2-3-2-5-7-6-5-3-8-9-5-3-2-5-7
#xy= 6-5-3-8-9-5-3-2-5-7-1-4-6-4-2-6-9-7-5-3-2-3-2-5-7

    


if __name__ == "__main__":
    main()