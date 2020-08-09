class Binary:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def height(A):
    if A == None:
        return 0
    else:
        ldepth = height(A.left)
        rdepth = height(A.right)

        if(ldepth > rdepth):
            return 1+rdepth
        return 1+ldepth

root = Binary(1)
root.left = Binary(2)
root.right = Binary(3)
root.left.left = Binary(4)
root.left.right = Binary(5)
root.left.left.left = Binary(7)
root.right.right = Binary(8)

print(height(root))


