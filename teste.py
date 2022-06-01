from Node import Node
from MinHeap import MinHeap
from PriorityQueue import PriorityQueue
import math
import numpy as np
from random import random


def correct_heap(heap):
    for i, node in enumerate(heap.nodes):
        left    = 2 * i + 1
        right   = 2 * i + 2
        if left < len(heap.nodes):
            if heap.nodes[left].key < node.key:
                return False

        if right < len(heap.nodes):
            if heap.nodes[right].key < node.key:
                return False

    return True

def convert_base(number, base):
    digits = []

    if number == 0:
        return 0
    
    while number != 0:
        digits.append(number % base)
        number = number//base  

    digits.reverse()
    return int(''.join([str(digit) for digit in digits]))


def make_queue(size):
    Nodes = []
    total_letters = 26
    a = 97

    for i in range(size):
        i_base = convert_base(i, total_letters)
        data = ''.join([chr(int(j)+a) for j in str(i_base)])
        key = int(random()*size)
        Nodes.append(Node(data, key))
    
    return PriorityQueue(Nodes)

## tests

number_tests = 100

for i in range(number_tests):
    # creating queue
    queue = make_queue(100)
    assert correct_heap(queue.heap), "created wrong queue"

    # adding element
    queue.put(Node('add', 0))
    assert correct_heap(queue.heap), "put went wrong" 

    # getting element
    lowest = queue.get()
    assert 0 == lowest.key, "didnt get the lowest node"
    assert correct_heap(queue.heap), "get went wrong"
    
    # changing key when element exists
    queue.put(Node('change', 10))
    queue.update_key('change', 1)
    assert queue.heap.nodes[queue.heap.find('change')].key == 1, "change key went wrong"

    # removing elemtn
    queue.put(Node('remove', 100))
    queue.remove('remove')
    assert queue.heap.find('remove') == -1, "didnt remove"

