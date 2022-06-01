from Node import Node
from MinHeap import MinHeap


class PriorityQueue:
    def __init__(self, elements = []):
        self.heap = MinHeap(elements)
    
    def get(self):
        # remove and return node with highest priority (lowes key value)
        return self.heap.pop()

    def put(self, node):
        # puts a node in the queue
        self.heap.push(node)

    def update_key(self, data, new_key):
        # updates the key of a node given by data
        node_index = self.heap.find(data)
        if node_index < 0:
            return -1
        self.heap.nodes[node_index].key = new_key
        self.heap.heapify(0)
        
    
    def list_nodes(self):
        # prints all the pairs data,key in order
        for node in self.heap.nodes:
            print(node.data, node.key)

    def remove(self, data):
        # removes a node given by data
        node_index = self.heap.find(data)
        if node_index < 0:
            return -1
        
        self.heap.nodes[node_index] = self.heap.nodes[-1]
        self.heap.nodes = self.heap.nodes[:-1]
        self.heap.down_heapify(node_index)
