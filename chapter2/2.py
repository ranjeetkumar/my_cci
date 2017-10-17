# find the kth to last element of a singly linked list
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
    
    def naive_kth(self,k):
        length = 0
        current = self.head
        while current:
           length += 1 
           current = current.next
        target_element = length - k
        current = self.head
        count = 0
        while count < target_element:
           current = current.next
           count += 1
        print (current.data)
    
    def kth(self,k):
        count = 0
        current = self.head
        while k>count:
            current = current.next
            count += 1
        tracker = self.head
        while current:
              current = current.next
              tracker = tracker.next
        print (tracker.data)
   
    def k_recursevely(self, k):
        return self.k_recurse(k, self.head)

    def k_recurse(self, k, x):
        if x is None:
            return  0
        count = self.k_recurse(k, x.next ) + 1
        if count == k:
            print (x.data)
        return count
 
if __name__ == "__main__":
    ll = SingleList()
    ll.add("1")
    ll.add("2")
    ll.add("3")
    ll.add("4")
    ll.print()
    ll.kth(2)
    ll.naive_kth(2)
    ll.k_recursevely(3)

