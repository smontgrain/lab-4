import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)


BinTree: TypeAlias = Optional["Node"]

@dataclass(frozen = True)
class Node:
    value: Any
    left: BinTree
    right: BinTree

@dataclass(frozen = True)
class BinarySearchTree:
    comes_before: Callable[[Any, Any], bool]
    tree: BinTree


#retuns true if the BST is empty, false otherwise
def is_empty(BST: BinarySearchTree) -> bool:
    match BST.tree:
        case None:
            return True
        case Node(_, _, _):
            return False
        
#Inserts value into its correct place in the tree
def insert(BST: BinarySearchTree, val: Any) -> BinarySearchTree:
    def helper(subtree: BinTree, val: Any, comes_before: Callable[[Any, Any], bool]) -> BinTree:
        match subtree:
            case None:
                return Node(val, None, None)
            case Node(value, left, right):
                if comes_before(val, value):
                    return Node(value, helper(left, val, comes_before), right)
                else:
                    return Node(value, left, helper(right, val, comes_before))
    return BinarySearchTree(BST.comes_before, helper(BST.tree, val, BST.comes_before))



#returns true if the given value is found in the tree
def lookup(BST: BinarySearchTree, val: Any) -> bool:
    def helper(subtree: BinTree, val: Any, comes_before: Callable[[Any, Any], bool]) -> bool:
        match subtree:
            case None:
                return False
            case Node(value, left, right):
                if not comes_before(val, value) and not comes_before(value, val):
                    return True
                elif comes_before(val, value):
                    return helper(left, val, comes_before)
                else: 
                    return helper(right, val, comes_before)
    return helper(BST.tree, val, BST.comes_before)




#deletes a value from the tree and moves things to fill in the gap
def delete(BST: BinarySearchTree, val: Any) -> BinarySearchTree:
    def equal(a: Any, b: Any) -> bool:
        return not BST.comes_before(a, b) and not BST.comes_before(b, a)

    # Return the largest value in the tree
    def highest_value(subtree: BinTree) -> Any:
        match subtree:
            case None:
                raise ValueError
            case Node(value, _, None):
                return value
            case Node(_, _, right):
                return highest_value(right)

    # deles the highest value
    def delete_highest_value(subtree: BinTree) -> BinTree:
        match subtree:
            case None:
                raise ValueError
            case Node(value, left, None):
                return left
            case Node(value, left, right):
                return Node(value, left, delete_highest_value(right))

    # Deletes the root of the subtree
    def delete_root(subtree: BinTree) -> BinTree:
        match subtree:
            case None:
                return None
            case Node(_, left, right):
                if left is None:           
                    return right
                left_max = highest_value(left)
                new_left = delete_highest_value(left)
                return Node(left_max, new_left, right)

    # Deletes the value
    def delete_value_from_bst(subtree: BinTree) -> BinTree:
        match subtree:
            case None:
                return None
            case Node(root_v, left, right):
                if equal(val, root_v):
                    return delete_root(subtree)
                elif BST.comes_before(val, root_v):
                    return Node(root_v, delete_value_from_bst(left), right)
                else:                       
                    return Node(root_v, left, delete_value_from_bst(right))

    return BinarySearchTree(BST.comes_before, delete_value_from_bst(BST.tree))