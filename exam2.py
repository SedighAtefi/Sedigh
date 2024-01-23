class btnode:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = left
        self.right = right
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
    def levelorder(self):
        