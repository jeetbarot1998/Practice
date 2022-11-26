class _Node:
    __slot__ = ['_left', '_root','_right']

    def __init__(self, element, left, right):
        self._left = left
        self._root = element
        self._right = right