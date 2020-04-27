class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def __setitem__(self, k, v):
        self.put(k, v)

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else: 
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.LeftChild)
        else:
            return self._get(key, currentNode.rightChild)
        
    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
    
    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)
    
    def remove(self, currentNode):
        if currentNode.isLeaf(): #被删节点没有子节点
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        
        
        else: #被删节点有一个子节点
            if currentNode.hasLeftChild: #被删节点的子节点在左侧
                if currentNode.isLeftChild(): #被删节点是某个节点的左节点
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild: #被删节点是某个节点的右节点
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: #被删节点是根节点，把左子节点升为根节点
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                    currentNode.leftChild.payload,
                    currentNode.leftChild.leftChild,
                    currentNode.leftChild.rightChild)
            else: #被删节点的子节点在右侧
                if currentNode.isLeftChild(): #被删节点是某个节点的左节点
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild: #被删节点是某个节点的右节点
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: #被删节点是根节点，把右子节点升为根节点
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                    currentNode.righttChild.payload,
                    currentNode.rightChild.leftChild,
                    currentNode.rightChild.rightChild)




class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.isLeftChild)

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.RightChild == self

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild
        
    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                """ 下面相当于做了递归调用
                self.leftChild.__iter__()
                """
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem