import sys
import unittest
from typing import *
from dataclasses import dataclass
import math
import time
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *
TREES_PER_RUN : int = 10000
#def example_graph_creation() -> None:
#    # Return log-base-2 of 'x' + 5.
#    def f_to_graph( x : float ) -> float:
#        return math.log2( x ) + 5.0
#    # here we're using "list comprehensions": more of Python's
#    # syntax sugar.
#    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
#    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
#    # Could have just used this type from the start, but I want
#    # to emphasize that 'matplotlib' uses 'numpy''s specific array
#    # type, which is different from the built-in Python array
#    # type.
#    x_numpy : np.ndarray = np.array( x_coords )
#    y_numpy : np.ndarray = np.array( y_coords )
#    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
#    plt.xlabel("X")
#    plt.ylabel("Y")
#    plt.title("Example Graph")
#    plt.grid(True)
#    plt.legend() # makes the 'label's show up
#    plt.show()
#if (__name__ == '__main__'):
#    example_graph_creation()

def random_tree(n: int) -> BinarySearchTree:
    bst = BinarySearchTree(comes_before, None)
    for _ in range(n):
        val = random.random()
        bst = insert(bst, val)
    return bst

def height(subtree: BinTree) -> int:
    match subtree:
        case None:
            return 0
        case Node(_, left, right):
            return 1 + max(height(left), height(right))

def average_height(n: int) -> float:
    total = 0
    for _ in range(TREES_PER_RUN):
        bst = random_tree(n)
        total += height(bst.tree)
    return total / TREES_PER_RUN
        
n_max = 50
#start_time = time.perf_counter()
#for _ in range(TREES_PER_RUN):
#    bst = random_tree(n_max)       
#    h = height(bst.tree)           
#end_time = time.perf_counter()
#elapsed_time = end_time - start_time
#print(f"Total time: {elapsed_time:.4f} seconds")



def plot_average_height(n_max: int) -> None:
    num_samples = 50
    Ns = np.linspace(0, n_max, num_samples, dtype=int)
    Ns = np.unique(Ns)
    Ys = [average_height(int(n)) for n in Ns]
    x = Ns.astype(int)
    y = np.array(Ys)
    plt.plot(x, y, marker='o', markersize=4, label=f'Average BST Height')
    plt.xlabel("N (Number of Nodes)")
    plt.ylabel("Average Tree Height")
    plt.title(f"Average Height vs Tree Size (Each Averaged Over {TREES_PER_RUN} Trees)")
    plt.grid(True)
    plt.legend()
    plt.show()



def average_insert_time(n: int) -> float:
    total = 0.0
    for _ in range(TREES_PER_RUN):
        total += time_one_insert(n)
    return total / TREES_PER_RUN

def time_one_insert(n: int) -> float:
    bst = random_tree(n)
    x = random.random()
    t0 = time.perf_counter()
    _ = insert(bst, x)
    t1 = time.perf_counter()
    return t1 - t0



#start_time = time.perf_counter()
#for _ in range(TREES_PER_RUN):
#    bst = time_one_insert(n_max)        
#end_time = time.perf_counter()
#elapsed_time = end_time - start_time
#print(f"Total time: {elapsed_time:.4f} seconds")


def plot_average_insert_time(n_max: int) -> None:
    num_samples = 100
    Ns = np.linspace(0, n_max, num_samples, dtype=int)
    Ns = np.unique(Ns)
    Ys = [average_insert_time(int(n)) for n in Ns]
    x = Ns.astype(int)
    y = np.array(Ys)
    plt.plot(x, y, marker='o', markersize=4, label=f'Average Insert Time')
    plt.xlabel("N (Number of Nodes)")
    plt.ylabel("Average Time to Insert")
    plt.title(f"Average Time to Insert Random Intiger (Each Averaged Over {TREES_PER_RUN} Trees)")
    plt.grid(True)
    plt.legend()
    plt.show()
if (__name__ == '__main__'):
    plot_average_insert_time(n_max)
    plot_average_height(n_max)