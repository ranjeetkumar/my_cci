#Delete Middle Node
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
    def delete(self,n):
        n.data = n.next.data
        n.next   = n.next.next    
    
 
if __name__ == "__main__":
    ll = SingleList()
    ll.add("1")
    ll.add("2")
    ll.add("3")
    ll.add("4")
    ll.print()
    print(ll.head.next.data)
    ll.delete(ll.head.next)
    ll.print()

