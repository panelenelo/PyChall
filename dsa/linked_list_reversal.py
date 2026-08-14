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




def main():
    linkl = deque()
    linkl.append(1)
    linkl.append(2)
    linkl.append(4)
    linkl.append(7)
    linkl.append(3)
    linked_list_reversal_i(linkl)
    ic(linkl)



    
    

    









if __name__ == "__main__":
    main()