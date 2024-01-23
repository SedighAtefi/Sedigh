class btnode:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
class nodeBST :
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
# n = btnode(1,btnode(2),btnode(3,None,btnode(4)))
class btree:
    def __init__(self,root = None):
        self.root = root
    def inorder(self,root):#LNR
        if root == None:
            return
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def postorder(self,root):#LRN
        if root == None : 
            return 
        else:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
    def preorder(self):
        pass

#درخت جستوجوی دودویی BST  Binary Search Tree
# مقدار پدر از فرزند سمت راست کمتر و از فرزند سمت چپ بیشتر است 
def searchBST(root,k):
    if root is None or root.key == k :
        return root
    if k > root.key : 
        return searchBST(root.right,k)
    return searchBST(root.left,k)
def insertBST(root,k):
    if root is None : 
        return nodeBST(k)
    if k < root.key : 
        root.left = insertBST(root.left,k)
    else : 
        root.right = insertBST(root.right,k)
    return
def minvalueBST(root):
    if root is None : 
        return root
    while root.left is not None : 
        root = root.left
    return root.key
def minnodeBST(r):
        if r.left is None : 
            return r
        else:
            minnodeBST(r.left)
            
#درخت heap 
def heapify(a,k):
    left = 2*k+1
    right = 2*k+2
    if left < len(a) and a[left] < a[k]:
        s = 1 
    else:
        s = k
    if right < len[a] and a[right] < a[s]:
        s = right
    if s != k : 
        a[k],a[s] = a[s],a[k]
        heapify(a,s)
#ساختن درخت  minheap 
def build_min_heap(a):
    n = int(len(a) // 2 - 1 )
    for k in range(n,-1,-1):
        heapify(a,k)
