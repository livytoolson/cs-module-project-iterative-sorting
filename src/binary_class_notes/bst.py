# Binary Search Tree
# ------------------

class ListNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# return True if we find node, return False if node is not found
# ITERATIVE SEARCH -->
def search(root, value):
    cur = root                  # always want root pointer to stay on root, cur is the one that will move around

    while cur is not None:
        # compare to see if we found the node
        if cur.value == value:
            return True         # True, we found it

        # if not, go to the proper next node to search
        if value < cur.value:
            cur = cur.left
        else:                   # value > cur.value
            cur = cur.right
        
    # If we make it here, we didn't find the node we were looking for
    return False

# RECURSIVE SEARCH --> 
def search_recur(cur, value):
    if cur is None:
        return False

    if cur.value == value:
        return True             # found it!
    
    if value < cur.value:
        return search_recur(cur.left, value)

    else:
        return search_recur(cur.right, value)
     
# pseudo code -->
# search for a node:
    # check if this node is what we're looking for
    # if the value we want is less than the current:
        # return search for node(left)
    # else:
        # return search for node(right)

# find the max depth of a tree
def max_depth(root):
    if root is None:
        return 0

    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    return max(left_depth, right_depth) + 1

# Print out BST values in order from least to greatest
def in_order(cur):
    if cur is None:
        print("Hit a none")
        return
    
    print("Going left")
    in_order(cur.left)          # Go left as far as we can
    print(cur.value)
    print("Going right")
    in_order(cur.right)

        
# Setting up the binary tree 
root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)
root.right.right = TreeNode(5)
root.right.right.right = TreeNode(6)

print(max_depth(root))

"""
in_order(root)

print(search(root, 2))
print(search(root, 5))
print(search(root, 99))

print(search_recur(root, 2))
print(search_recur(root, 5))
print(search_recur(root, 99))
"""