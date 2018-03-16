#Sum_list
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

    def add_to_beginning(self, value):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def sum_lists(self,ll_a, ll_b):
        n1 =  ll_a.head
        n2 =  ll_b.head
        carry = 0

        while n1 or n2:
          result = carry
          if n1:
            result += n1.data
            n1 = n1.next
          if n2:
            result += n2.data
            n2 = n2.next

          ll3.add(result % 10)
          carry = result // 10

        if carry:
          ll3.add(carry)
    
    def sum_lists_followup(self,ll_a, ll_b):
        
        if len(ll_a) < len(ll_b):
           for i in range(len(ll_b) - len(ll_a)):
            ll_a.add_to_beginning(0)
        else:
           for i in range(len(ll_a) - len(ll_b)):
            ll_b.add_to_beginning(0)

        n1 =  ll_a.head
        n2 =  ll_b.head
        result = 0
        while n1 and n2:
           result = (result * 10) + n1.data + n2.data
           n1 = n1.next
           n2 = n2.next

        for i in str(result):
            ll4.add(int(i))

    
       
    
 
if __name__ == "__main__":
    ll1 = SingleList()
    ll1.add(7)
    ll1.add(1)
    ll1.add(6)
    ll2 = SingleList()
    ll2.add(5)
    ll2.add(9)
    ll2.add(2)
    ll3 = SingleList()
    ll3.sum_lists(ll1,ll2)
    ll3.print()
    ll4 = SingleList()
    ll5 = SingleList()
    ll5.add(6)
    ll5.add(1)
    ll5.add(7)
    ll6 = SingleList()
    ll6.add(2)
    ll6.add(9)
    ll6.add(5)
    ll4.sum_lists_followup(ll5,ll6)
    ll4.print()
