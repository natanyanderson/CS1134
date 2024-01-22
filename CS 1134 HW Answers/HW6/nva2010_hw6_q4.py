from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList()
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        new_lnk_lst.add_last(current.data)
        current = current.next
    return new_lnk_lst

def deep_copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList()
    if not(isinstance(lnk_lst,DoublyLinkedList)):
        return lnk_lst
    else:
        for elem in lnk_lst:
            val = deep_copy_linked_list(elem)
            new_lnk_lst.add_last(val)
    return new_lnk_lst