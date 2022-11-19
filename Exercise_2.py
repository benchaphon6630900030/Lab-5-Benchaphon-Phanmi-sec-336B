class TreeNode:
    def __init__(self, data):
      self.left = l = None
      self.right = r = None
      self.data = data
      
class Tree:
    def __init__(self):
        self.root = None

    def height(root):
        if root is None:
            return 0 
        return max(height(root.l), height(root.r)) + 1
        
    def getcolumn(h):
        if g == 1:
            return 1
        return getcolumn(g-1) + getcolumn(g-1) + 1
    
    def print_Tree(A, root, column, row, height):
        if root is None:
            return
        A[row][column] = root.data
        print_Tree(A, root.l, column-pow(2, height-2),row+1, height-1)
        print_Tree(A, root.r, column+pow(2, height-2),row+1, height-1)
        
    def TreePrinter():
        g = height(mineTree.root)
        column = getcolumn(g)
        A = [[0 for _ in range(column)] for __ in range(g)]
        print_Tree(A, mineTree.root, column//2, 0, g)
        for i in A:
            for j in i:
                if j == 0:
                    print(" ",end="")
                else:
                    print(j,end="")
            print(" ")
            
mineTree = Tree()
mineTree.root = TreeNode(50)
mineTree.root.l = TreeNode(25)
mineTree.root.r = TreeNode(75)
mineTree.root.l.l = TreeNode(30)
mineTree.root.l.r = TreeNode(40)
mineTree.root.r.l = TreeNode(60)

TreePrinter()
