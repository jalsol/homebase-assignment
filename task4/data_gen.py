from hierarchical_node import HierarchicalNode

import sqlite3
import shortuuid
import random


MAX_DEPTH = 5
MAX_CHILDREN = 10


def counter_generator():
    i = 1
    while True:
        yield i
        i += 1

counter = counter_generator()

def generate_children(node, depth):
    if depth >= MAX_DEPTH:
        return
    for _ in range(random.randint(0, MAX_CHILDREN)):
        child = HierarchicalNode(next(counter), shortuuid.uuid(), node)
        node.add_child(child)
    
    for child in node.children:
        generate_children(child, depth + 1)

def fill_table(conn, node):
    c = conn.cursor()
    c.execute("INSERT INTO hierarchy VALUES (?, ?, ?)", (node.id, node.uuid, node.parent.id if node.parent else None))
    conn.commit()

    for child in node.children:
        fill_table(conn, child)

def generate_data():
    root = HierarchicalNode(next(counter), shortuuid.uuid())
    generate_children(root, 0)

    conn = sqlite3.connect("data.sqlite")

    fill_table(conn, root)

if __name__ == "__main__":
    generate_data()