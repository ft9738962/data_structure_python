class BinHeap: 
    def __init__(self):
        self.heapList = [0] #为了后面完全二叉树节点计算方便，将heaplist的序号0节点初始化为0
        self.currentSize = 0

    """将新数据插入列表末尾后，会影响该条节点路径的大小顺序，因此需要对其调整，将新数据项上浮到该条路径合适的位置，这个操作不会影响其它位置的数据大小关系
    """
    def percUp(self, i):
        while i // 2 > 0: #在未到达根节点之前
            if self.heapList[i] < self.heapList[i // 2]: #如果新节点小于其父节点，则交换
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2 #更换完更新新数据的位置，继续比较
        
    def insert(self, k):
            self.heapList.append(k) #添加到末尾
            self.currentSize = self.currentSize + 1
            self.percUp(self.currentSize)

    """在实施delMin()方法后，为了填补删除根节点后的空缺，将最后的子节点提升上来，因为其可能比左右的子节点大，因此要在路径上比较，将其放置在合适的位置，这个过程称为下沉
    """
    def perDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        #比较输入节点的子节点哪个小并返回节点序号
            if i * 2 + 1 > self.currentSize:
                return i * 2
            else:
                if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                    return i * 2
                else:
                    return i * 2 + 1

    def delMin(self):
            retval = self.heapList[1] #移走堆顶
            self.heapList[1] = self.heapList[self.currentSize]
            self.currentSize = self.currentSize - 1
            self.heapList.pop()
            self.perDown(1) #新顶下沉
            return retval

    #生成二叉树堆
    def buildHeap(self, alist):
        i = len(alist) // 2 #从最后节点的父节点开始，因为叶节点是不需要去下沉的
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        print(len(self.heapList), i)
        while (i > 0):
            print(self.heapList, i)
            self.percDown(i)
            i = i - 1
        print(self.heapList, i)