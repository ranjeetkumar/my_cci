#Palindrome
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
    
    def is_palindrome(self):
        fast = slow = ll.head
        stack = []

        while fast and fast.next:
          stack.append(slow.data)
          slow = slow.next
          fast = fast.next.next

        if fast:
          slow = slow.next

        while slow:
           top = stack.pop()
           if top != slow.data:
            return False
           slow = slow.next

        return True
    
 
if __name__ == "__main__":
    ll = SingleList()
    ll.add(3)
    ll.add(1)
    ll.add(3)
    ll.print()
    print (ll.is_palindrome())
    

