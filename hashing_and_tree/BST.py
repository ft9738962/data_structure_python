class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor = 0

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
        return self.parent and self.parent.rightChild == self

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

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin() #找右子树的最小节点
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.righttChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def spliceOut(self): #把找到的继承节点摘出来
        if self.isLeaf(): #如果是叶节点
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren(): #
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

"""
================================================================
"""

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
        
        elif currentNode.hasBothChildren(): #被删节点有两个子节点
            succ = currentNode.findSuccessor() #寻找继承节点
            succ.spliceOut() #把继承节点的相关节点断开重连
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        
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

"""
====================================================================
"""

class AVLTree(BinarySearchTree):
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else: 
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0: #平衡后父节点平衡因子不为0，说明平衡导致了左/右子树的高度发生了变化
                self.updateBalance(node.parent) #递归向上调整父节点

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0: #节点右重，子节点左重时
                self.rotateRight(node.rightChild) #先右旋子节点
                self.rotateLeft(node) #再左旋节点
            else: #节点右重，子节点没有左重
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot): #左旋，旧节点命名为rotRoot
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild #新根左节点放到旧根右节点
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot(): #如果旧节点是根节点
            self.root = newRoot #将新节点设为根节点
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot #旧根节点设为新根节点的左子节点
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + \
            1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + \
            1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot): #右旋，旧节点命名为rotRoot
        newRoot = rotRoot.leftChild
        rotRoot.rightChild = newRoot.rightChild #新根右节点放到旧根左节点
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot(): #如果旧节点是根节点
            self.root = newRoot #将新节点设为根节点
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot #旧根节点设为新根节点的左子节点
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - \
            1 + min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - \
            1 - max(rotRoot.balanceFactor, 0)