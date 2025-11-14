import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *





class BSTTests(unittest.TestCase):
    def test_numeric(self):
        t = BinarySearchTree( comes_before, None )
        t = insert(t, 6)
        t = insert(t, 4)
        t = insert(t, 9)
        t = insert(t, 12)
        empty_tree = (BinarySearchTree( comes_before, None ))
        self.assertEqual(t, BinarySearchTree( comes_before, Node(6, Node(4, None, None), Node(9, None, Node(12, None, None)))))
        self.assertEqual(is_empty(empty_tree), True)
        self.assertEqual(is_empty(t), False)
        self.assertEqual(lookup(t, 4), True)
        self.assertEqual(lookup(t, 5), False)
        t_deleted = delete(t, 9)
        self.assertEqual(t_deleted, BinarySearchTree( comes_before, Node(6, Node(4, None, None), Node(12, None, None))))
        self.assertEqual(delete(t, 7), t)
        self.assertEqual(delete(t, 6), BinarySearchTree( comes_before, Node(4, None, Node(9, None, Node(12, None, None)))))
    
    def test_string(self):
        t = BinarySearchTree( comes_before, None )
        t = insert(t, "fruit")
        t = insert(t, "apple")
        t = insert(t, "banana")
        t = insert(t, "pineapple")
        self.assertEqual(t, BinarySearchTree( comes_before, Node("fruit", Node("apple", None, Node("banana", None, None)), Node("pineapple", None, None))))
        self.assertEqual(lookup(t, "apple"), True)
        self.assertEqual(lookup(t, "pear"), False)
        t_deleted = delete(t, "banana")
        self.assertEqual(t_deleted, BinarySearchTree( comes_before, Node("fruit", Node("apple", None, None), Node("pineapple", None, None))))
        self.assertEqual(delete(t, "pear"), t)
        self.assertEqual(delete(t, "fruit"), BinarySearchTree( comes_before, Node("banana", Node("apple", None, None), Node("pineapple", None, None))))

    def test_euclidean(self):
        @dataclass(frozen = True)
        class Point2:
            x: float
            y: float
        def point_before(a: Point2, b: Point2) -> bool:
            da = a.x*a.x + a.y*a.y
            db = b.x*b.x + b.y*b.y
            return da < db if da != db else (a.x, a.y) < (b.x, b.y)
        t = BinarySearchTree( point_before, None )
        t = insert(t, Point2(3,3))
        t = insert(t, Point2(7,3))
        t = insert(t, Point2(1,0))
        t = insert(t, Point2(2,2))
        self.assertEqual(t, BinarySearchTree( point_before, Node(Point2(3,3), Node(Point2(1,0), None, Node(Point2(2,2), None, None)), Node(Point2(7,3), None, None))))
        self.assertEqual(lookup(t, Point2(1,1)), False)
        self.assertEqual(lookup(t, Point2(3,3)), True)
        t_deleted = delete(t, Point2(2,2))
        self.assertEqual(t_deleted, BinarySearchTree( point_before, Node(Point2(3,3), Node(Point2(1,0), None, None), Node(Point2(7,3), None, None))))




if (__name__ == '__main__'):
    unittest.main()
