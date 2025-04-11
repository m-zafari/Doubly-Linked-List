# Mohammad Zafari
# mhdzafari80@gmail.com

class Node: 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None 
        self.prev = None  
         
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def push(self, new_data): 

        new_node = Node(new_data) 

        new_node.next = self.head 
   
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node  
    
    def count_nodes(self): 
        temp = self.head 
        if self.head is not None: 
            count = 0
            while(True): 
                count += 1 
                temp = temp.next
                if (temp == None): 
                    return count
        else:
            return 0

    def print_dll(self):
        node = self.head
        while node is not None:
            print(f"{node.data}", end=" ")
            node = node.next
        print()

    def del_same_value(self):
        first = self.head
        second = first.next
        while second is not None:
            while second is not None:
                if first.data == second.data:
                    if second.next is None:
                        second.prev.next = None
                        return
                    else:
                        second.prev.next = second.next
                        second.next.prev = second.prev
                second = second.next
            first = first.next
            second = first.next

"""
list1 = DoublyLinkedList()
list1.push(12)
list1.push(12)
list1.push(10)
list1.push(8)
list1.push(8)
list1.push(6)
list1.push(4)
list1.push(4)
list1.push(4)
list1.push(4)

list1.del_same_value()
list1.print_dll()
"""