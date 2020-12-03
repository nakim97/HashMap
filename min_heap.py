# Course: CS261 - Data Structures
# Assignment: 5
# Student: Na Kim
# Description: This written program will implement the MinHeap class through the methods:
# add,get_min,remove_min, and build_heap.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        this function will add a new object to the minHeap maintaining the heap property
        """
        # put new element at the end of array
        self.heap.append(node)

        # if minHeap is empty, return
        if self.heap.length() == 1:
            return

        child = self.heap.length() - 1 # inserted element
        parent = (child - 1) // 2  # inserted element's parent index

        # if the value of the parent is  > value of inserted element, swap and repeat + within range
        while parent >=0:
            if self.heap.get_at_index(child) < self.heap.get_at_index(parent):
                self.heap.swap(parent, child)
                child = parent
                parent = (child - 1) // 2
            else:
                break
        return

    def get_min(self) -> object:
        """
        this function returns an object with a minimum key without removing the object from the heap
        """
        # if the heap is empty, raise a custom exception
        if self.heap.length() ==0:
            raise MinHeapException
        # if the heap if not empty, return minimum key
        return self.heap.get_at_index(0)



    def helper_remove(self, index):
        """
        this function (percolating down) is a helper function for remove_min
        """
        # initialize and set up index for left and right children
        left_child = (2 * index) + 1
        right_child = (2 * index) + 2
        min_val = index

        # if within boundaries and if left child is less than current index, set as min
        if left_child <= self.heap.length()-1 and self.heap.get_at_index(left_child) < self.heap.get_at_index(min_val):
            min_val = left_child
        # if within boundaries and if right child is elss than current index, set as min
        if right_child <= self.heap.length()-1 and self.heap.get_at_index(right_child) < self.heap.get_at_index(min_val):
            min_val = right_child

        if min_val != index:
            self.heap.swap(index, min_val)
            self.helper_remove(min_val)

    def remove_min(self):
        """
        this function will return an object with a minimum key and remove it from the heap
        """
        # if the heap is empty, raise a custom exception
        if self.is_empty():
            raise MinHeapException()

        val = self.get_min() # store the min key
        pos = self.heap.pop()

        if self.heap.length() == 0: # min
            return val

        self.heap.set_at_index(0, pos)  # set and pop value to remove min
        self.helper_remove(0)

        return val  # remove min and return min val

    def helper_build(self, index):
        """
        this function is a helper function for build heap function (percolate up)
        """
        while index >=0:
            # initialize and set up index for left and ride children
            left_child = (2 * index) + 1
            right_child = (2 * index) + 2
            min_val = index

            # if within boundaries and if left child is less than current index, set as min
            if left_child <= self.heap.length() - 1 and self.heap.get_at_index(left_child) < self.heap.get_at_index(
                    min_val):
                min_val = left_child
            # if within boundaries and if right child is elss than current index, set as min
            if right_child <= self.heap.length() - 1 and self.heap.get_at_index(right_child) < self.heap.get_at_index(
                    min_val):
                min_val = right_child

            if min_val != index:
                self.heap.swap(index, min_val) # swap
                index = (index - 1) // 2  # parent node
                self.helper_build(min_val)
            index-=1
        return

    def build_heap(self, da: DynamicArray) -> None:
        """
        this function will receive a dynamic array with objects in any order and builds a minHeap
        """
        # set up and initialize new Dynamic Array
        d_val = DynamicArray()

        if da.length()==0:
            return

        for i in range(da.length()):
            d_val.append(da.get_at_index(i))

        self.heap = d_val

        # the index of the first non leaf element from back of array
        pos = ((da.length()// 2))

        for i in range(pos, -1, -1):
            self.helper_build(pos)

        self.heap = d_val



# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
