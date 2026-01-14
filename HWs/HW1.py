"""
This homework is designed to get you warmed up and familiar with Python syntax
and pythonic thinking. Before each function you will see a comment with the 
problem number and the concepts I think you need in order to complete the 
problem. The docstrings will give you a description of what each function's 
intended behavior is and the doctests will ultimately give you the best examples
of what a function's behavior looks like. 

In order to test your function to see if it's working, open a terminal, navigate
to the directory that this file is in, and run `python -m doctest HW1.py` or 
`python -m doctest -v HW1.py` for more info. 
Reminder, you will need to use python3 on MacOS.
"""

# 1. python built in functions
def new_max(a, b):
    """
    Write a function that takes in two integers and returns the bigger of the 
    two. You may use an existing funcion. 

    >>> new_max(1, 5)
    5
    >>> new_max(5, 5)
    5
    """
    pass

# 2. for loops, built in functions
def lowercase_strings(strings):
    """
    Write a function that takes in a list of strings. Return a new list 
    containing the strings from the original list that are all lowercase. 

    >>> lowercase_strings([])
    []
    >>> lowercase_strings(["hello", "Hello"])
    ["hello"]
    """
    pass

# 3. while loops
def count_down(n):
    """
    Write a function that takes a positive integer n and prints each number from
    n down to 0, one per line.
    You must use a while loop.

    >>> count_down(5)
    5
    4
    3
    2
    1
    0
    """
    pass

# 4. dictionaries
def count_ints(lst):
    """
    Write a function that takes in a nested list of either integers or an 
    iterable containing integers, return a dictionary counting how many times 
    each integer appears. Elements may be nested at any level. 

    >>> count_ints([])
    {}
    >>> count_ints([1, 2, 1, 1])
    {1: 3, 2: 1}
    >>> count_ints([1, [2, 1], [[1], 3], 3])
    {1: 3, 2: 1, 3: 2}
    """
    pass

# 5. sets and iteration
def all_substrings(s):
    """
    Return a set of all substrings of the given string s.

    >>> all_substrings('abc')
    {'', 'a', 'b', 'c', 'ab', 'bc', 'abc'}

    EXTRA CREDIT: Do this in a single line of code. (will be graded manually)
    """
    pass

# 6. tuples and dicts
def tuplize(d):
    """
    Convert a dictionary into a list of tuples where each tuple is
    in the format (key, value).

    >>> tuplize({"a": 1, "b": "hello", "c": 3})
    [("a", 1), ("b", "hello"), ("c", 3)]

    """
    pass

# 7. lists
def extract_and_apply(l, p, f):
    '''
    Implement the function below in a single line:

        def extract_and_apply(l, p, f):
            result = []
            for x in l:
                if p(x):
                    result.append(f(x))
            return result

    where l is a list, 
    p is a predicate (a function that returns a boolean),
    and f is a function.

    Do this in a single line. Multi-line functions' points will be removed.
    
    >>> extract_and_apply([], lambda x: x % 2 == 0, lambda x: x * 2)
    []
    >>> extract_and_apply([1, 2, 3, 4, 5], lambda x: x % 2 == 0, lambda x: x * 2)
    [4, 8]
    
    '''
    pass

# 8. Higher order functions
def apply_f_n_times(f, x, n):
    """
    Write a function that takes in a function (whose domain is one integer) and
    2 integers. Your function should then apply the function to the first 
    integer the second integer number of times.

    >>> apply_f_n_times(lambda x: x + 1, 5, 1)
    6
    >>> apply_f_n_times(lambda x: x + 1, 5, 10)
    15
    >>> apply_f_n_times(lambda x: x, 5, 10)
    5
    """
    pass

# 9. Generators
def generate_fibonacci():
    '''
    Create a generator that yields the Fibonacci sequence.
    Remember that the fibonacci sequence is the result of adding the previous
    two numbers in the sequence.

    >>> gen = generate_fibonacci()
    >>> [next(gen) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    '''
    pass

# 10.
'''
Now, we're going to implement a binary search tree. But we're going 
to do so in a way that makes it behave like a native Python object!
For reference: https://en.wikipedia.org/wiki/Binary_search_tree
or chapters 6 & 7 of https://www.cis.upenn.edu/~cis120/current/files/1200notes.pdf

The goal is to be able to do the following types of "native" 
actions on a BSTree t by leveraging magic methods:

1. Check if an element exists in the tree

if elem in t:
    ...

2. Iterate over the sorted elements of the tree

for elem in t:
    ...

3. Print out the tree nicely

print(t)

For our tree, we will only need to implement insertion, not deletion. 
'''
class BSTree:
    
    def __init__(self):
        '''
        Constructor should return an empty BSTree.
        '''
        pass

    def __contains__(self, element):
        '''
        Determine if element is in the tree. Should return True if so,
        and False otherwise. This magic method allows us to use the syntax

        >>> element in t

        You should iterate through the BST, do not instantiate a list.
        '''
        pass
    
    def __iter__(self):
        '''
        Return a generator (that means yield!) of the elements 
        visited in an in-order traversal:
        https://en.wikipedia.org/wiki/Tree_traversal

        Note that for a binary search tree, in-order traversal results in
        the sorted order of the elements.

        This will allow us to traverse the BSTree nicely like:
        
        >>> for elem in t:
        >>>    ...

        and even cast it like
        
        list(t)
        '''
        pass

    def __str__(self):
        '''
        Return a string representation of the tree as (left, elem, right)
        where elem is the element stored at the root, and left and right
        are the string representations of the left and right subtrees
        (which are in the same format). Empty trees should be represented 
        as a hyphen.

        For example, if we had a BSTree like:
                7
              /  \
             3   9
            / \
           1  5

        the string representation would be

        "(((-, 1, -), 3, (-, 5, -)), 7, (-, 9, -))"
        '''
        pass

    def insert(self, element):
        '''
        Insert the given element into the tree. If the element is equal to
        an element already in the tree, raise an exception with the message:
        'Cannot insert duplicate element!'
        '''
        pass


class Node(object):
    '''
    A node of the BSTree. 
    Should contain a value, left subtree, and right subtree.
    You may find it useful to define some additional methods here.
    '''
    pass


