class NestedSetNode:
    def __init__(self, id, uuid, left=None, right=None, parent=None):
        self.id = id
        self.uuid = uuid
        self.left = left
        self.right = right
        self.parent = parent
        self.children = []
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        print(f'Added child {child.id} to parent {self.id}')