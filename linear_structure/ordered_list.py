from unordered_list import Node

class OrderedList:
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def isEmpty(self):
        return self.head == None

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

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        prev = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                prev = current
                current = current.getNext()

        temp = Node(item)
        if prev == None: #插入在表头的情况
            temp.setNext(self.head)
            self.head = temp
        else: #插入在表中
            temp.setNext(current)
            prev.setNext(temp)