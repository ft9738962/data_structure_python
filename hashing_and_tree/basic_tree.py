from ..linear_structure.stack import Stack

'''
二叉树
'''
class BinaryTree2:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree2(newNode)
        else:
            t = BinaryTree2(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree2(newNode)
        else:
            t = BinaryTree2(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def setRootVal(self, val):
        self.key = val

    def getRootVal(self):
        return self.key

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree2('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree) #下降前将节点推入栈
            currentTree = currentTree.getLeftChild() #将当前节点设为子节点
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop() #弹出父节点
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop() #出栈上升
        else:
            raise ValueError
    return eTree
