class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return False
        if self.head.data == data:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

    def display(self):
        if self.is_empty():
            print("List is empty")
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" --> ".join(elements))


my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(5)
my_linked_list.append(8)
my_linked_list.prepend(0)
my_linked_list.display()
my_linked_list.delete(5)
my_linked_list.display()