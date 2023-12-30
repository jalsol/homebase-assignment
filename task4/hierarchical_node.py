class HierarchicalNode:
    def __init__(self, id, uuid, parent=None):
        self.children = []
        self.id = id
        self.uuid = uuid
        self.parent = parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        print(f'Added child {child.id} to parent {self.id}')