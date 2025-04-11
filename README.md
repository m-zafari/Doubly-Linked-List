# Doubly-Linked-List
print_dll ---> print the data of doubly linked list
del_same_value ---> delete nodes with same data

# example:
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

output:
4 6 8 10 12 
