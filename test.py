class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
            newnode.next = None
            newnode.prev = None
        else:
            temp = self.tail
            self.tail.next = newnode
            newnode.prev = temp
            newnode.next = None
            self.tail = newnode
        self.length +=1



    def __str__(self):
        temp = self.head
        string = ""
        while temp is not None:
            string += str(temp.data)
            if temp.next is not None:
                string+=str("->")
                string+=str("<-")
            temp = temp.next
        return string



# DDL = DoubleLinkedList()
# DDL.append(12)
# DDL.append(13)
# DDL.append(14)
# print(DDL)



list = [1,2,4,5,7,8,0,3,6,7]


def findpair(arr, target):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:

                if arr[i] + arr[j] ==  target:
                    print(arr[i], arr[j])

p = findpair(list, 7)
print(p)
