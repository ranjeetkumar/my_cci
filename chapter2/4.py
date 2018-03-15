#Partition
class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.next = None

class SingleList(object):

    head = None
    tail = None
    
    def print(self):
        x = self.head
        while x is not None:
            print(x.data,end='')
            print(" -> ",end='')
            x = x.next
        print(None)

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def partition(self, x):
      current = self.tail = self.head
      while current:
        nextNode = current.next
        current.next = None
        if current.data < x:
            current.next = self.head
            self.head = current
        else:
            self.tail.next = current
            self.tail = current
        current = nextNode
        
      if self.tail.next is not None:
         self.tail.next = None
    
 
if __name__ == "__main__":
    ll = SingleList()
    ll.add(3)
    ll.add(1)
    ll.add(5)
    ll.add(8)
    ll.add(5)
    ll.add(10)
    ll.add(2)
    ll.add(1)
    ll.print()
    ll.partition(5)
    ll.print()

