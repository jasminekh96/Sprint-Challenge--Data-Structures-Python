from doubly_linked_list import DoublyLinkedList
# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer.

# _You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == None:
            self.current = self.storage.head
        if self.storage.length < self.capacity: 
            # insert item to linked list
            self.storage.add_to_tail(item)

        elif self.storage.length == self.capacity:
            removed_head = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if removed_head == self.current:
                self.current = self.storage.tail

# The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current = self.current
        list_buffer_contents.append(current.value)
        if current.next:
            node = current.next
        else:
            node = self.storage.head
        while node is not current:
            list_buffer_contents.append(node.value)
            if node.next:
                node = node.next
            else:
                node = self.storage.head
        return list_buffer_contents

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
