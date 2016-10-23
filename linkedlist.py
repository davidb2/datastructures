from node import SinglePointerNode as Node

class SinglyLinkedList:
    def __init__(self):
        self._size = 0
        self._head = None
    def prepend(self, value):
        '''Prepends a value to the linked list. O(1)'''
        self._head = Node(value, self._head)
        self._size += 1
    def drop(self):
        '''Drops head of the linked list. O(1)'''
        if self._head != None:
            self._head = self._head.next
            self._size -= 1
    def head(self):
        '''Gets the of the linked list. O(1)'''
        return self._head
    def find(self, value):
        '''Tries to find the index of the value given. O(n)'''
        temp = self._head
        index = 0
        while temp != None:
            if temp.data == value:
                return index
            temp = temp.next
            index += 1
        return None
    def concat(self, other):
        '''Concats the linked list to the end of self. O(n)'''
        if not isinstance(other, SinglyLinkedList):
            raise TypeError('operand +: not defined for SinglyLinkedList and {}'.format(type(other)))
        if self._head == None:
            return other
        elif other._head == None:
            return self
        self._size = len(self) + len(other)
        temp = other._head
        while temp.next != None:
            temp = temp.next
        temp.next = self._head
        self._head = other._head
    def __len__(self):
        '''Gets the length of the linked list. O(1)'''
        return self._size

    def __iter__(self):
        '''Returns an iterable of the linked list.'''
        temp = self._head
        while temp != None:
            yield temp.data
            temp = temp.next
    def __str__(self):
        '''Returns a string representation of the linked list.'''
        return str(list(self))
s = SinglyLinkedList()
s.prepend(1)
s.prepend(2)
s.prepend(3)
print(len(s))
for x in s:
    print x
s.prepend(4)
print s
p = SinglyLinkedList()
p.prepend(10)
p.prepend(20)
s.concat(p)
print s
print len(s)
print s.find(11)