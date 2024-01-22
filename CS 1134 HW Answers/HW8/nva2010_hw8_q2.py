from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for i in range(1, n+1):
        bst.insert(i)
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst, low, high):
    if low == ((high//2)+1):
        bst.insert(low)
        add_items(bst, low+1, high)
    elif low > high:
        return bst
    elif low > ((high//2)+1):
        bst.insert(low)
        add_items(bst, low+1, high)
    else:
        add_items(bst, low+1, high)
        bst.insert(low)