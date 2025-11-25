
class Node:
    def __init__(self,data):# self It makes sure each object keeps its own data.
        self.data = data
        self.next = None

# Creating a Link list class --------
class linklist:
    def __init__(self):
        self.head = None
    # We can insert value into Beginning ------------
    def insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # We can insert value into End ------------
    def insert_at_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # We can insert value into After Node ------------
    def insert_after_node(self,terget_node,data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == terget_node:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    # We can Delete value  ------------
    def delete_node(self,terget_data):
        if not self.head:
            return
        if self.head == terget_data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == terget_data:
                current.next = current.next.next
                return
            current = current.next

    # We can search value  ------------
    def Search_data(self,terget_data):
        current = self.head
        while current:
            if current.data == terget_data:
                return True
            current = current.next
        return False

    # For Display values  ------------
    def display(self):
        current = self.head
        while current:
            print(current.data,end=" --> ")
            current = current.next
        print("None")


LL=linklist()
LL.insert_at_beginning(5)
LL.insert_at_beginning(4)
LL.insert_at_beginning(3)
LL.insert_at_beginning(1)
LL.insert_at_end(10)
LL.insert_after_node(1,2)
LL.insert_after_node(5,6)
LL.insert_after_node(6,6)
LL.delete_node(6)
print(LL.Search_data(5))
print(LL.Search_data(7))

LL.display()