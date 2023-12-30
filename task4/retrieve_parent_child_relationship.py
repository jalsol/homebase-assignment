import sqlite3


def retrieve_parent_child_relationship():
    conn = sqlite3.connect("data.sqlite")
    c = conn.cursor()
    result = c.execute("SELECT * FROM nested_set ORDER BY lft ASC").fetchall()

    parent_ids = [None] * len(result)
    id_rgt_stack = [] # stack of (id, rgt)

    for (id, uuid, node_lft, node_rgt) in result:
        # if a.rgt < node_lft then a is not an ancestor of node
        while id_rgt_stack and id_rgt_stack[-1][1] < node_lft:
            id_rgt_stack.pop()
        
        # now all `rgt` values in the stack are greater or equal to `node_lft`
        # thus, all nodes in the stack are ancestors of the current node
        # the last node in the stack is the parent of the current node
        if id_rgt_stack:
            parent_ids[id - 1] = id_rgt_stack[-1][0]

        id_rgt_stack.append((id, node_rgt))

    for (id, uuid, _, _) in result:
        print(f'id {id} ({uuid}) is a child of id {parent_ids[id - 1]}')


if __name__ == "__main__":
    retrieve_parent_child_relationship()