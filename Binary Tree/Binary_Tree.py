class _Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def maketree(self, e, left, right):
        self._root = _Node(e,left._root,right._root)

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot._element,end=' ')
            self.inorder(troot._right)

    def preorder(self,troot):
        if troot:
            print(troot._element,end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)

    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element, end=' ')

    def levelorder(self):
        pass

    def count(self,troot):
        if(troot):
            x = self.count(troot._left)
            y = self.count(troot._right)
            return x + y + 1
        return 0

    def height(self,troot):
        if(troot):
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0
    
    def insert(self, troot,e):
        temp = None
        while troot:
            # if a temperory root exists
            temp = troot
            # temp has the node element
            if e == troot._element:
                return
            elif e < troot._element:
                # assign respective child to troot and reach the destination
                troot = troot._left
            elif e > troot._element:
                # assign respective child to troot and reach the destination
                troot = troot._right
        # reached the leaf node where we have to insert the new node and "temp" has the reference to the node
        n = _Node(e)
        # if the tree is not empty then
        if self._root:
            # check on which side of the leaf node we have to insert
            if e < temp._element:
                temp._left = n
            else:
                temp._right = n
        # if the tree is empty then
        else:
            self._root = n
    
    def rinsert(self,troot,e):
        # recursive calls until troot is not null.
        if troot:
            if e < troot._element:
                troot._left = self.rinsert(troot._left,e)
            elif e > troot._element:
                troot._right = self.rinsert(troot._right,e)
        # Once we have found the location to insert, troot becomes null and no recursive calls,
        # we enter the else part and insert the new node there.
        else:
            n = _Node(e)
            troot = n
        return troot
    
    def search(self, key):
        troot = self._root
        while troot:
            if troot._element == key:
                return True
            elif key > troot._element:
                troot = troot._right
            elif key < troot._element:
                troot = troot._left
        return False

    def rsearch(self, troot, key):
        if troot:
            if key == troot._element :
                return True
            elif key > troot._element:
                return self.rsearch(troot._right,key)
            elif key < troot._element:
                return self.rsearch(troot._left,key)
        else:
            return False

    def delete(self,key):
        # parent
        p = self._root
        # parent of parent
        pp = None
        while p and p._element != key:
            pp = p
            if key < p._element:
                p = p._left
            else:
                p = p._right
        # object p has the refrence to node.
        # element not found.
        if not p:
            return False
        #  If the node has right and let child both.
        if p._left and p._right:
            # choose the largest element from left subtree
            subtree = p._left
            psubtree =  p
            while subtree._right:
                psubtree = subtree
                subtree = subtree._right
            p._element = subtree._element
            p = s
            pp = psubtree




            

'''
reference of structure of tree below.    
        10
    20      30
'''

x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
emptyNode = BinaryTree()
# start by making leaf nodes
x.maketree(20,emptyNode,emptyNode)
y.maketree(30,emptyNode,emptyNode)
z.maketree(10,x,y)
print(z.inorder(z._root), 'inroder')
print(z.preorder(z._root), 'preorder')
print(z.postorder(z._root), 'postorder')

'''
reference of structure of tree below.    
            10
    20              30
40              50      
                    60
'''

x = BinaryTree() #40
y = BinaryTree() #60
z = BinaryTree() #20
r = BinaryTree() #50
s = BinaryTree() #30
t = BinaryTree() #10
emptyNode = BinaryTree() #empty node
x.maketree(40,emptyNode,emptyNode)
y.maketree(60,emptyNode,emptyNode)
z.maketree(20,emptyNode,x)
r.maketree(50,emptyNode,y)
s.maketree(30,r,emptyNode)
t.maketree(10,z,s)
print('Inorder Traversal')
t.inorder(t._root)
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print()
print('count',t.count(t._root))
print('height',t.height(t._root))


# BST: MAKE A TREE USING INSERT
print('==== MAKE BST WITH INSERTION ====')
B = BinaryTree()
B.insert(B._root,50)
B.insert(B._root,30)
B.insert(B._root,80)
B.insert(B._root,10)
B.insert(B._root,40)
B.insert(B._root,60)
B.insert(B._root,70)
print('Inorder Traversal')
B.inorder(B._root)
print()


# BST: MAKE A TREE USING RECURSION
print('==== MAKE BST WITH RECURSION ====')
B = BinaryTree()
B._root = B.rinsert(B._root,50)
B.rinsert(B._root,30)
B.rinsert(B._root,80)
B.rinsert(B._root,10)
B.rinsert(B._root,40)
B.rinsert(B._root,60)
B.rinsert(B._root,70)
print('Inorder Traversal')
B.inorder(B._root)
print()


# BST SEARCH:
elem = 60
print(f'Searching for the element {elem} in BST')
print('result = ', B.search(elem))

print('result = ', B.rsearch(B._root,elem))

# Deleting a node:
B = BinaryTree()
B._root = B.rinsert(B._root,40)
B.rinsert(B._root,12)
B.rinsert(B._root,15)
B.rinsert(B._root,65)
B.rinsert(B._root,60)
B.rinsert(B._root,63)
B.rinsert(B._root,52)
B.rinsert(B._root,45)
B.rinsert(B._root,56)
B.rinsert(B._root,90)
B.rinsert(B._root,95)
B.rinsert(B._root,70)
print('Inorder Traversal')
B.inorder(B._root)
print()
B.delete(65)
print('Inorder Traversal')
B.inorder(B._root)
print()