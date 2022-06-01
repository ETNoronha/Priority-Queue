# Priority-Queue

I implemented three classes. `PriorityQueue` implements a priority queue based on a min-heap. It has the common methods for a queue: `get()` and `put()`, as well the `update_key()` and two others, `list_nodes()` and `remove()`, which are good for testing.

The class `MinHeap` implements the min-heap instatiated by `PriorityQueue`. It takes an unordered array of `Node` and builds a min-heap with `heapify()`. This function is recursive and works by guaranteeing that all nodes below the lowest unresolved node are in a min-heap, and then resolving said node. It also implements simple `push()`, `pop()` and `find()` methods. 

Finally, `Node` implements a generic data type with carries a `data` value and a `key` value. The former could represent the name of an edge in a graph and the second its cost, for example. 

#

The file `test.py` implements a testing routine which goes over several different cases and corner cases.
