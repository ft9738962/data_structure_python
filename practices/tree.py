'''
给定一种序列化二叉树的方式：
从根节点起始按层次遍历二叉树所有“可能”存在节点的位置：
若该位置存在节点，则输出节点值，
并在下一层相应增加两个可用位置；
否则输出None，且不增加下一层的可用位置。

输入格式:
一行合法的Python表达式，可解析为包含整数与None的列表

输出格式：
二叉树中序遍历的整数序列，以空格分隔

输入样例：
[5, 4, 7, 3, None, 2, None, -1, None, 9]

输出样例：
-1 3 4 5 9 2 7
'''

'''
将列表变成树再中序遍历
'''
class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
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

def seq2tree(seq):
    seq = [0] + seq
    root = BinaryTree(None)
    treeList = [0, root]
    for i in range(1, len(seq)):
        r = treeList[i]
        if seq[i]:
            r.setRootVal(seq[i])
            if len(treeList) < len(seq):
                r.insertLeft(None)
                treeList.append(r.getLeftChild())
            if len(treeList) < len(seq):
                r.insertRight(None)
                treeList.append(r.getRightChild())
    return root

def inorderTree(root):
    if root and root.getRootVal():
        return inorderTree(root.getLeftChild()) + \
            [str(root.getRootVal())] + \
            inorderTree(root.getRightChild())
    else:
        return []
        
t1 = [5, 4, 7, 3, None, 2, None, -1, None, 9]
print(' '.join(inorderTree(seq2tree(t1))))

t2 = [5,1,4,None,None,3,6]
print(inorderTree(seq2tree(t2)))

'''
给定一个二叉树，请给出它的镜面翻转。
为方便起见，本题只给出完全二叉树的层次遍历，请给出相应的翻转二叉树的中序遍历。
'''
from math import floor, log2

def mirror_flip(lst):
    lst = [lst[x] for x in range(len(lst)) if x % 2 == 0]
    height = floor(log2(len(lst))) + 1
    if height == 1:
        return [0] + lst
    new_lst = [0, lst[0]] #初始化新列表
    lst = [0] + lst #原表补0号位数据，方便迭代
    for i in range(2, height + 1):
        add_lst = lst[2 ** i - 1: 2 ** (i - 1) - 1: -1]
        new_lst += add_lst
    return new_lst

def inorder_parse(lst, i):
    if i < len(lst):
        return inorder_parse(lst, 2 * i) + list(lst[i]) + inorder_parse(lst, 2 * i + 1)
    else:
        return []

a = eval(input())
b = mirror_flip(a)
c = inorder_parse(b, 1)
print(' '.join(c))