# augmented BBST for line segment intersection algorithm 
# from Segment import Segment

class InternalNode():
    def __init__(self, key):
        self.key = key
        self.value = None
        self.left = NilNode.instance() 
        self.right = NilNode.instance()
        self.parent = NilNode.instance() 
    
    def __bool__(self):
        return True 
    
    def __nonzero__(self):
        return True 
    
    def isLeaf(self):
        return False
    
    def isInternal(self):
        return True

class LeafNode(): # segment + LL node 
    def __init__(self, key, segment):
        self.key = key
        self.value = segment
        self.prev = NilNode.instance() # Leaf Node
        self.next = NilNode.instance() # Leaf Node
        self.parent = NilNode.instance() # InternalNode

    def isLeaf(self):
        return True

    def __bool__(self):
        return True 
    
    def __nonzero__(self):
        return True 
    
    
    def isInternal(self):
        return False


class NilNode():
    __instance__ = None 
    def instance(self):
        if (self.__instance__ is None):
            self.__instance__ = NilNode()
        return self.__instance__
    
    def __init__(self):
        self.key = None
        self.left = None 
        self.right = None 
        self.parent = None 

    def __bool__(self):
        return False 
    
    def __nonzero__(self):
        return False 


class BBST(): 

    def __init__(self):
        self.root = NilNode.instance()
        self.head = NilNode.instance() # LeafNode 
        self.tail = NilNode.instance() # LeafNode 
        self.size = 0

    def insert(self, key, value):
        node = LeafNode(key, value)
        self.__insert_helper(node)

    
    def __insert_helper(self, newNode):
        # Traverse down the tree to find where to insert it
        parentNode = NilNode.instance()
        currentNode = self.root
        while (currentNode):
            parentNode = currentNode
            if (newNode.key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        # empty tree, root's parent is null
        if (not parentNode):    
            self.root = newNode 
        # parent node is already an internal node
        elif (parentNode.isInternal()): 
            newNode.parent = parentNode
            if (newNode.key < parentNode.key):
                parentNode.left = newNode # become parent's left child 
                myRightSib = parentNode.right # rework LL pointers 

                myLeftSib = NilNode.instance()
                if (myRightSib.prev):
                    myLeftSib = myRightSib.prev 

                newNode.prev = myLeftSib
                newNode.next = myRightSib

                if (myLeftSib):
                    myLeftSib.next = newNode 
                else:   # new head of list
                    self.head = newNode
                myRightSib.prev = newNode

            else: 
                parentNode.right = newNode # become parent's right child 
                myLeftSib = parentNode.left # rework LL pointers 

                myRightSib = NilNode.instance()
                if (myLeftSib.next):
                    myRightSib = myLeftSib.next

                newNode.prev = myLeftSib
                newNode.next = myRightSib

                if (myRightSib):
                    myRightSib.prev = newNode 
                else:   # new end of list
                    self.tail = newNode
                myLeftSib.next = newNode

        # deal with rotating leaves 
        else: # parent node is a Leaf node 
            if (newNode.key < parentNode.key):

            else: # (newNode.key > parentNode.key):
                newInternal = InternalNode(parentNode.key)
                newInternal.left = parentNode
                newInternal.right = newNode
                newInternal.parent = parentNode.parent

                myLeftSib = parentNode

                myRightSib = NilNode.instance()
                if (myLeftSib.next):
                    myRightSib = myLeftSib.next
                
                newNode.prev = myLeftSib
                newNode.next = myRightSib

                if (myRightSib):
                    myRightSib.prev = newNode 
                else:   # new end of list
                    self.tail = newNode
                myLeftSib.next = newNode
        
        self.size += 1
