from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    root = prefix_lst[0]
    if len(prefix_lst) == 1:
        root = prefix_lst[0]
        bst.insert(root)
        return bst
    high = len(prefix_lst) - 1
    for i in range(len(prefix_lst)):
        if prefix_lst[i] > root:
            high = i - 1
            break
    rootnode = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(root))
    if high != len(prefix_lst) - 1:
        right_side = restore_helper(prefix_lst, root, high + 1, len(prefix_lst) - 1)
    else:
        right_side = None
    left_side = restore_helper(prefix_lst, root, 1, high)
    rootnode.left = left_side
    rootnode.right = right_side
    if left_side != None:
        left_side.parent = rootnode
    if right_side != None:
        right_side.parent = rootnode
    bst.root = rootnode
    return bst


def restore_helper(lst, root, low, high):
    if low == high:
        return BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[low]))
    else:
        node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[low]))
        if low + 1 > high:
            leftie = None
        else:
            leftie = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[low + 1]))

        if low + 2 > high:
            rightie = None
        elif lst[low + 2] > lst[low]:
            rightie = restore_helper(lst, root, low + 2, high)
            leftie = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(lst[low + 1]))
        else:
            leftie = restore_helper(lst, root, low + 1, high)
            rightie = None
        node.left = leftie
        node.right = rightie
        if leftie != None:
            leftie.parent = node
        if rightie != None:
            rightie.parent = node
        return node