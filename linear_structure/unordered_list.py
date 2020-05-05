class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext

"""
=====================================================
"""

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
            if previous == None: #previous为空说明current在第一项就找到了被查数
                self.head = current.getNext() #直接将head指向current的下一个节点，即相当于移除了head
            else: #若在表中段找到被查数
                previous.setNext(current.getNext()) #将current的下一个节点与previous节点链接，把current节点抛弃

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        temp = Node(item)
        if self.head:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        else:
            self.head = temp

    def index(self, item):
        count = 0
        current = self.head
        while current != None:
            if current.getData() == item:
                return count
            else:
                current = current.getNext()
                count = count + 1
        return None

    def insert(self, pos, item):
        temp = Node(item)
        count = 0
        current = self.head
        while count < pos:
            prev = current
            current = current.getNext()
            count = count + 1
        temp.setNext(current)
        prev.setNext(temp)

    def pop(self):
        current = self.head
        if current != None:
            while current.getNext() != None:
                prev = current
                current = current.getNext()
            prev.setNext(None)
            return current.getData()
        else:
            return None

    def pop(self, pos):
        count = 0
        current = self.head
        if pos == 0 and self.head:
            data = current.getData
            self.head.setNext(None)
            return data
        elif not self.head:
            return None
        else:
            prev = None
            while current != None and count <= pos:
                if count == pos and prev:
                    if current.getNext():
                        prev.setNext(current.getNext())
                    else:
                        prev.setNext(None)
                    return current.getData()
                else:
                    prev = current
                    current = current.getNext()
                    count = count + 1