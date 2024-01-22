from DoublyLinkedList import *
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged):
        if s1 == srt_lnk_lst1.trailer and s2 == srt_lnk_lst2.trailer:
            return
        elif s1 == srt_lnk_lst1.trailer:
            merged.add_last(s2.data)
            s2 = s2.next
        elif s2 == srt_lnk_lst2.trailer:
            merged.add_last(s1.data)
            s1 = s1.next
        elif s1.data < s2.data:
            merged.add_last(s1.data)
            s1 = s1.next
        elif s2.data < s1.data:
            merged.add_last(s2.data)
            s2 = s2.next
        elif s2.data == s1.data:
            merged.add_last(s2.data)
            merged.add_last(s1.data)
            s1 = s1.next
            s2 = s2.next
        merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged)
    if srt_lnk_lst1.is_empty():
        return srt_lnk_lst2
    elif srt_lnk_lst2.is_empty():
        return srt_lnk_lst1
    s1 = srt_lnk_lst1.first_node()
    s2 = srt_lnk_lst2.first_node()
    merged = DoublyLinkedList()
    merge_helper(srt_lnk_lst1, srt_lnk_lst2, s1, s2, merged)
    return merged
