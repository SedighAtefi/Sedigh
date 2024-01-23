class dnode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dlinkedlist:
    def __init__(self):
        self.head = None

    def display(self):
        t = self.head 
        while t is not None:       
            print(t.data, end=" <----> ") 
            t = t.next
        print(None)

    def addinstart(self, data):
        n = dnode(data)
        if self.head is not None:
            n.next = self.head
            self.head.prev = n
        self.head = n

    def addinend(self, data):
        n = dnode(data)
        if self.head is not None:
            t = self.head
            while t.next is not None: 
                t = t.next
            t.next = n 
            n.prev = t
        else:
            self.head = n

    def swap_first_and_last(self):
        if self.head is None or self.head.next is None:
            return

        first_node = self.head
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        first_node.data, last_node.data = last_node.data, first_node.data



# Example usage:
dlink = dlinkedlist()
dlink.addinstart(5)
dlink.addinstart(9)
dlink.addinstart(8)
dlink.addinstart(4)
dlink.addinstart(1)

print("Original list:")
dlink.display()

dlink.swap_first_and_last()

print("List after swapping first and last nodes:")
dlink.display()
