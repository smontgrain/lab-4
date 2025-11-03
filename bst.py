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



def is_empty(BST: BinarySearchTree) -> bool:
    match BST.tree:
        case None:
            return True
        case Node(_, _, _):
            return False
        
def insert(BST: BinarySearchTree, val: int) -> BinarySearchTree:




def lookup(BST: BinarySearchTree, val: int) -> bool:





def delete(BST: BinarySearchTree, val: int) -> BinarySearchTree: