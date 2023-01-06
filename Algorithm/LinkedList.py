class Node:
    def __init__(self, data, next=None):
        self.data = data  # 데이터 저장
        self.next = next  # 링크 저장

    def __str__(self):
        return str(self.data)

    def printAll(self):
        print(self.data)
        while self.next:
            self = self.next
            print(self.data)

    def addNode(self, data):
        while self.next:
            self = self.next
        self.next = Node(data)

    def deleteNode(self, data):
        if self.data == data:
            self= self.next
        else:
            while self.next:
                if self.next.data == data:
                    self.next = self.next.next
                else:
                    self = self.next

    def searchNode(self, data):
        if self.data == data:
            return self
        else:
            while self.next:
                if self.next.data == data:
                    return self.next
                else:
                    self = self.next
        print("No such data")
        return None


a = Node(1)
a.addNode(2)
a.addNode(3)
a.addNode(4)
a.addNode(5)
a.addNode(6)
a.addNode(7)
a.searchNode(4).printAll()
print("")
a.deleteNode(4)
a.searchNode(4).printAll()
