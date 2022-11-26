class _Node:
    __slot__ = ['_element', '_next']

    def __init__(self, element, nextelem):
        self._element = element
        self._next = nextelem


class linkedList:
    def __init__(self):
        # Initially the linked list will be of len 0, has no head and tail
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def addfirst(self, e):
        if self.isempty():
            newest = _Node(e, None)
            self._head = newest
            self._tail = newest
        else:
            newest = _Node(e, self._head)
            self._head = newest
        self._size += 1

    def addlast(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def addany(self, index, e):
        p = self._head
        i = 0
        if index > self._size:
            return self.addlast(e)

        elif self.isempty() or index == 0:
            self.addfirst(e)

        else:
            while p:
                if index == i:
                    newest = _Node(e, p._next)
                    p._next = newest
                    self._size += 1
                    break
                i += 1

    def removefirst(self):
        # only delete if the length is not 0
        if self.isempty():
            print('List is empty')
            return
        e = self._head._element
        self._head = self._head._next
        self._size -= 1
        # If the length is 0 now, then set the tail as None
        if self.isempty() or self._size == 1:
            self._tail = None
        return e

    def removelast(self):
        # only delete if the length is not 0
        if self.isempty():
            print('List is empty')
            return
        index = 1
        # If the length is 1, then set the head,tail as None and size as 0
        if self._size == 1:
            element_deleted = self._head._element
            self._tail = None
            self._head = None
            self._size = 0
            return element_deleted
        p = self._head
        # traverse to the 2nd last element of the linked list
        while index < self._size - 1:
            p = p._next
            index += 1
        # Now we are the 2nd last node of the linked list
        element_deleted = p._next._element
        self._tail = p
        self._tail._next = None
        self._size -= 1
        return element_deleted

    def removeany(self,index):
        if self.isempty():
            print('List is empty')
            return
        i = 1
        if index == 1:
            return  self.removefirst()
        elif index == self._size:
            return self.removelast()  
        if index not in range(1,self._size):
            return 'list index out of range'
        
        p = self._head
        while i < index - 1:
            p = p._next
            i += 1
        # Now we are the previous node of the element to deleted
        element_deleted = p._next._element
        p._next = p._next._next
        return element_deleted

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

    def search(self, key):
        p = self._head
        index = 0
        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1
        return -1


L = linkedList()
L.addlast(7)
L.display()
print('length is', len(L))
L.addlast(18)
L.addlast(3)
L.display()
print('length is', len(L))
value_to_search = 12
print(f'searched index of {value_to_search} is:', L.search(value_to_search))
# L.addfirst(1)
# L.display()
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.addfirst(9)
# L.display()
L.addany(0, 99)
L.display()
print('length is', len(L))
print('Element removefirst is', L.removefirst())
L.display()
print('line 154: length is', len(L))
print('line 155: Element removefirst is', L.removefirst())
L.display()
print('length is', len(L))
print('Element removelast is', L.removelast())
L.display()
print('line 160: length is', len(L))
print('line 161: Element removelast is', L.removelast())
L.display()
print('line 163: length is', len(L))
print('element removed using removeany is:', L.removeany(1))
L.display()
print('line 166: length is', len(L))

