from Node import Node

class MinHeap:
    def __init__(self, nodes = []):
        self.nodes = nodes
        self.heapify(root_index = 0)
        
    def pop(self):
        # return the node with the lowest key value
        # and remove it from the heap

        min_node = self.nodes[0]
        self.nodes[0] = self.nodes[-1]
        self.nodes = self.nodes[:-1]
        self.down_heapify(0)

        return min_node
        
    def push(self, element):
        # insert a node and corrects min heap

        self.nodes.append(element)
        #self.heapify(0)

        parent_index = (len(self.nodes)-2) // 2
        current_index = len(self.nodes)-1

        while self.nodes[current_index].key < self.nodes[parent_index].key and current_index != 0:
            self.nodes[current_index] = self.nodes[parent_index]
            self.nodes[parent_index] = element

            temp = parent_index
            parent_index = (parent_index-1)//2
            current_index = temp
            

    def find(self, data):
        # find the index of a node, gives its data value

        for i, node in enumerate(self.nodes):
            if node.data == data:
                return i
        return -1
        
    def down_heapify(self, root_index):
        # puts node[root_index] in the correct position in the heap,
        # assuming all other nodes below it are in the correct position

        if 2 * root_index + 1 > len(self.nodes)-1 :
            return
        else:
            lowest = root_index
            left    = 2 * root_index + 1
            right   = 2 * root_index + 2

            if self.nodes[left].key < self.nodes[lowest].key:
                lowest = left
            
            if right < len(self.nodes):
                if self.nodes[right].key < self.nodes[lowest].key:
                    lowest = right

            if lowest != root_index:
                lowest_node = self.nodes[lowest]
                self.nodes[lowest] = self.nodes[root_index]
                self.nodes[root_index] = lowest_node
                self.down_heapify(lowest)
            return

    def heapify(self, root_index):
        # makes a min heap from position root_index downwards

        if root_index >= len(self.nodes)//2:
            # if node is the last with children
            return
        else:
            self.heapify(root_index + 1)
            self.down_heapify(root_index)
            return