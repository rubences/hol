"""Minimal Cost Binary Search Trees
The description that follows presumes that you have completed Binary Search Trees. Before starting on this kata, fill in the code for Tree's __eq__, __ne__, and __str__ methods as described and verified by that kata.

Imagine you have a binary search tree and after some time you notice that some of the nodes are accessed more frequently than others. The time it takes to access a node depends on how deep the node is in the tree, so ideally you would want nodes that are accessed often placed close to the root. The purpose of the this kata is to "balance" the tree such that the average cost of accessing nodes is minimized.

Each node has a weight attribute which could represent how often the node is accessed. For each node in a tree, one can associate a cost, which is the weight of the node times its depth. The depth of the root node is defined to be 1, and the depth of a node directly below a node of depth d is d + 1. The cost of a tree is simply the sum of the costs of its nodes. Your first task is to write a function cost that takes a tree as argument and returns the cost of the tree.

Now we are getting to the more challenging part of this kata. Your final task is to write a function make_min_tree that takes a non-empty list of nodes as argument and returns a tree with minimal cost. The list passed as argument is sorted in ascending order. No two nodes in the list are equal (under the definition of "equal" provided by __eq__ and __ne__). For this last part, your code will be tested with lists up to a length of 100. (Note: My algorithm is quadratic in space and cubic in time, but I am not sure it cannot be done better.)"""

def cost(tree, depth=1):
    '''Returns the cost of a tree which root is depth deep.'''

    if tree.is_leaf():
        return tree.root.weight * depth
    else:
        return tree.root.weight * depth + cost(tree.left, depth + 1) + cost(tree.right, depth + 1)

def test():

    

class Tree(object):
    
    def __init__(self, root, left=None, right=None):
        assert root and type(root) == Node
        if left: assert type(left) == Tree and left.root < root
        if right: assert type(right) == Tree and root < right.root

        self.left = left
        self.root = root
        self.right = right
        
    def is_leaf(self):
        return not(self.left or self.right)
        
    
    def __str__(self):
        pass
    
    def __eq__(self, other):
        pass
    
    def __ne__(self, other):
        pass

class Node(object):
    
    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return '%s:%d' % (self.value, self.weight)   
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __eq__(self, other):
        return self.value == other.value 

    def __ne__(self, other):
        return self.value != other.value 


def cost(tree, depth=1):
    '''Returns the cost of a tree which root is depth deep.'''

    if tree.is_leaf():
        return tree.root.weight * depth
    else:
        return tree.root.weight * depth + cost(tree.left, depth + 1) + cost(tree.right, depth + 1)

def test():
    # Test cost
    assert cost(Tree(Node(1))) == 1
    assert cost(Tree(Node(1, 2))) == 2
    assert cost(Tree(Node(1), Tree(Node(0)))) == 2

    pass

def make_min_tree(node_list):
    '''
    node_list is a list of Node objects
    Pre-cond: len(node_list > 0) and node_list is sorted in ascending order
    Returns a minimal cost tree of all nodes in node_list.
    '''    

    # Base case
    if len(node_list) == 1:
        return Tree(node_list[0])

    # Recursive case
    else:



    pass