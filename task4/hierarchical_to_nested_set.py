from hierarchical_node import HierarchicalNode
from nested_set_node import NestedSetNode

import sqlite3


hierarchical_root = None
nested_set_root = None

def counter_generator():
    i = 1
    while True:
        yield i
        i += 1

counter = counter_generator()

def retrieve_data():
    nodes = []
    parent_ids = []

    conn = sqlite3.connect("data.sqlite")
    c = conn.cursor()

    for id, uuid, parent_id in c.execute("SELECT * FROM hierarchy ORDER BY id ASC"):
        nodes.append(HierarchicalNode(id, uuid))
        parent_ids.append(parent_id)
    
    for i, node in enumerate(nodes):
        if parent_ids[i] is not None:
            node.parent = nodes[parent_ids[i] - 1]
            node.parent.add_child(node)

    global hierarchical_root
    hierarchical_root = nodes[0]

def convert_node(hierarchical_node, nested_set_node):
    nested_set_node.left = next(counter)

    for child in hierarchical_node.children:
        nested_set_child = NestedSetNode(child.id, child.uuid, parent=nested_set_node)
        nested_set_node.add_child(nested_set_child)
        convert_node(child, nested_set_child)

    nested_set_node.right = next(counter)

def fill_table(conn, node):
    c = conn.cursor()
    c.execute("INSERT INTO nested_set VALUES (?, ?, ?, ?)", (node.id, node.uuid, node.left, node.right))
    conn.commit()

    for child in node.children:
        fill_table(conn, child)

def convert_hierarchical_to_nested_set():
    retrieve_data()
    
    global nested_set_root
    nested_set_root = NestedSetNode(hierarchical_root.id, hierarchical_root.uuid)
    convert_node(hierarchical_root, nested_set_root)

    conn = sqlite3.connect("data.sqlite")
    fill_table(conn, nested_set_root)
    

if __name__ == "__main__":
    convert_hierarchical_to_nested_set()