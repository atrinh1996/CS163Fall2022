
class TreeNode():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = NilNode().instance() 
        self.right = NilNode().instance()
        self.parent = NilNode().instance() 
        self.height = 0
    
    def __bool__(self):
        return True 
    
    def __nonzero__(self):
        return True 

    def value(self):
        return self.value


class NilNode(TreeNode):
    __instance__ = None 
    def instance(self):
        if (self.__instance__ is None):
            self.__instance__ = NilNode()
        return self.__instance__
    
    def __init__(self):
        self.key = None
        self.value = None
        self.left = None 
        self.right = None 
        self.parent = None 
        self.height = -1

    def __bool__(self):
        return False 
    
    def __nonzero__(self):
        return False 

class AVLTree(): 

    def __init__(self):
        self.root = NilNode().instance()
        self.size = 0

    def inorder(self):
        return self.__inorder_helper_recursive(self.root)
    
    def __inorder_helper_recursive(self, node):
        value_list = []
        if (node):
            left_list = self.__inorder_helper_recursive(node.left)
            # print(f'left_list: {left_list}')

            left_list.append(node.value)

            # print(f'left_list appended: {left_list}')

            right_list = self.__inorder_helper_recursive(node.right)
            # print(f'right_list: {right_list}')

            value_list = left_list + right_list
            # print(f'new value_list: {value_list}')
        
        # print(f'value_list return: {value_list}')
        return value_list



    def insert(self, key, value):
        node = TreeNode(key, value)
        self.__insert_helper(node)
    
    def insert_recursive(self, key, value):
        node = TreeNode(key, value)
        # print(f'Inserting: {value}, key: {key}')
        self.root = self.__insert_helper_recursive(NilNode().instance(), self.root, node)
        # if (self.root):
        #     print(f'Root not null')
        self.size += 1
    
    def remove_recursive(self, key):
        # print(f'Removing: key: {key}')
        self.root = self.__remove_helper_recursive(NilNode().instance(), self.root, key)
        self.size -= 1


    def __insert_helper(self, newNode):
        # Traverse down the tree to find where to insert it
        parentNode = NilNode().instance()
        currentNode = self.root
        while (currentNode):
            parentNode = currentNode
            if (newNode.key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        
        newNode.parent = parentNode
        if (not parentNode):
            self.root = newNode 
        else:
            if (newNode.key < parentNode.key):
                parentNode.left = newNode
            else: 
                parentNode.right = newNode
    
        
        self.size += 1

    def __insert_helper_recursive(self, parentNode, currentNode, newNode):
        # print(f'[__insert_helper_recursive] current node: {currentNode.value}')
        if (not currentNode):
            # print(f'[__insert_helper_recursive] hit a null, return new node {newNode.value}')
            return newNode 
        elif (newNode.key < currentNode.key):
            # print(f'[__insert_helper_recursive] current node: {currentNode.value}; go left')
            currentNode.left = self.__insert_helper_recursive(currentNode, currentNode.left, newNode)
        elif (newNode.key > currentNode.key):
            # print(f'[__insert_helper_recursive] current node: {currentNode.value}; go right')
            currentNode.right = self.__insert_helper_recursive(currentNode, currentNode.right, newNode)
        elif (newNode.key == currentNode.key):
            currentNode.left = self.__insert_helper_recursive(currentNode, currentNode.left, newNode)
            # return currentNode

        currentNode.height = 1 + max(self.heightOf(currentNode.left), self.heightOf(currentNode.right))

        currentNode = self.balance(parentNode, currentNode)
        # print(f'[__insert_helper_recursive] returning current node: {currentNode.value}')
        return currentNode

    def __remove_helper_recursive(self, parentNode, currentNode, key):
        if (not currentNode):
            # print(f'[__remove_helper_recursive] Note found. current seg: {currentNode.value}, key: {key}')
            return currentNode 
        elif (key < currentNode.key):
            # print(f'[__remove_helper_recursive] current seg: {currentNode.value}, key: {key}; go left')
            currentNode.left = self.__remove_helper_recursive(currentNode, currentNode.left, key)
        elif (key > currentNode.key):
            # print(f'[__remove_helper_recursive] current seg: {currentNode.value}, key: {key}; go right')
            currentNode.right = self.__remove_helper_recursive(currentNode, currentNode.right, key)
        elif (key == currentNode.key):
            # print(f'[__remove_helper_recursive] current seg: {currentNode.value}, key: {key}; matched')
            if (not currentNode.left): 
                # print(f'[__remove_helper_recursive] no left child, handing over right')
                currentNode.right.parent = parentNode
                return currentNode.right 
            elif (not currentNode.right):
                # print(f'[__remove_helper_recursive] no right child, handing over left')
                currentNode.left.parent = parentNode
                return currentNode.left
            else: 
                # print(f'[__remove_helper_recursive] remove from min of right subtree')
                minRightNode = self.get_min_right_subtree(currentNode.right)
                currentNode.value = minRightNode.value
                currentNode.key = minRightNode.key
                currentNode.right = self.__remove_helper_recursive(currentNode, currentNode.right, minRightNode.key)



        currentNode.height = 1 + max(self.heightOf(currentNode.left), self.heightOf(currentNode.right))

        currentNode = self.balance(parentNode, currentNode)
        return currentNode

    def heightOf(self, node):
        if (node):
            return node.height
        else: 
            return -1

    def balance(self, parentNode, node):
        # print(f'[balance] node {node.value}')
        if (not self.isLeaf(node)):
            # Left heavy 
            if (self.heightDiff(node) > 1):
                if (self.heightDiff(node.left) > 0): 
                    # print(f'[balance] LL unbalanced')
                    node = self.rotateRight(parentNode, node)
                else: 
                    # print(f'[balance] LR unbalanced')
                    node.left = self.rotateLeft(node, node.left)
                    node = self.rotateRight(parentNode, node)
            # Right heavy
            elif (self.heightDiff(node) < -1): 
                if (self.heightDiff(node.right) < 0): 
                    # print(f'[balance] RR unbalanced')
                    node = self.rotateLeft(parentNode, node)
                else: 
                    # print(f'[balance] RL unbalanced')
                    node.right = self.rotateRight(node, node.right)
                    node = self.rotateLeft(parentNode, node)

        return node 

    def isLeaf(self, node):
        return ((not node.left) and (not node.right))

    def heightDiff(self, node):
        leftHeight = self.heightOf(node.left)
        rightHeight = self.heightOf(node.right)

        return leftHeight - rightHeight

    def rotateRight(self, parentNode, node):
        # print(f'[rotateRight]')
        orig = node 

        node = node.left 
        orig.left = node.right 
        node.right = orig 

        orig.height = 1 + max(self.heightOf(orig.left), self.heightOf(orig.right))
        node.height = 1 + max(self.heightOf(node.left), self.heightOf(node.right))

        return node

    def rotateLeft(self, parentNode, node):
        # print(f'[rotateLeft]')
        orig = node 

        node = node.right 
        orig.right = node.left 
        node.left = orig 

        orig.height = 1 + max(self.heightOf(orig.left), self.heightOf(orig.right))
        node.height = 1 + max(self.heightOf(node.left), self.heightOf(node.right))

        return node
    
    def get_min_right_subtree(self, node):
        if (not node.left):
            # print(f'[get_min_right_subtree] returning Seg: {node.value}, key={node.key}')
            return node 
        
        return self.get_min_right_subtree(node.left)