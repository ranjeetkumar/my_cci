# Write code to remove duplicates from an unsorted linked list
# How would you solve this problem if a temporary buffer is not allowed?
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
    
    def remove_dups_withbuffer(self):
      if self.head is None:
        return

      current = self.head
      seen = set([current.data])
      while current.next:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next


    def remove_dups_withoutbuffer(self):
      if self.head is None:
        return

      current = self.head
      while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

     
if __name__== "__main__":
    ll = SingleList()
    ll.add("1")
    ll.add("2")
    ll.add("2")
    ll.print()
    ll.remove_dups_withbuffer()
    ll.print()

