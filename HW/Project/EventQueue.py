import heapq

class EventQueueNode():
    def __init__(self, key, value):
        self.key = key # priority of the node (the point itself)
        self.value = value 

    def __hash__(self):
        return hash(self.key)
    
    def __lt__(self, other):
        return self.key < other.key
    def __le__(self, other):
        return self.key <= other.key
    def __gt__(self, other):
        return self.key > other.key
    def __ge__(self, other):
        return self.key >= other.key
    def __eq__(self, other):
        return self.key == other.key
            
# a min heap on the coordinate of the point values
class EventQueue():
    def __init__(self):
        self.heap   = []    # priority queue heap
        self.S      = set() # set to ensure no duplicates in heap
    
    # keys are Point for the Line Seg intersection program
    def insert(self, key, value):
        node = EventQueueNode(key, value)
        if (not node in self.S):
            heapq.heappush(self.heap, node)
            self.S.add(node)
    
    def get(self):
        if (self.heap):
            return self.heap[0]
        else: 
            return None 
    
    def remove(self):
        if (self.heap):
            node = heapq.heappop(self.heap)
            self.S.remove(node)
            return node
        else: 
            return None 
    
    def empty(self):
        return not self.heap
