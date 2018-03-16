#Intersection
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


    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

def intersection(list1, list2):
      if list1.tail is not list2.tail:
        return False

      shorter = list1 if len(list1) < len(list2) else list2
      longer = list2 if len(list1) < len(list2) else list1

      diff = len(longer) - len(shorter)

      shorter_node, longer_node = shorter.head, longer.head

      for i in range(diff):
        longer_node = longer_node.next

      while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

      return longer_node    

    
       
    
 
if __name__ == "__main__":
    ll1 = SingleList()
    ll1.add(7)
    ll1.add(1)
    ll1.add(6)
    ll2 = ll1
    ll2.add(3)
    print (intersection(ll1,ll2).data)
