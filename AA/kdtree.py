class node:
    def __init__(self, value, left, right, parent, compare):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.compare = compare
        
def toggle_compare(variable):
    return variable^1
    
def insert_node(value):
    global root_node
    current_parent = root_node
    current_value = value
    current_compare = current_parent.compare
    parent_found = False
    
    while not parent_found:
        if current_value[current_compare] < current_parent.value[current_compare]:
            if current_parent.left is None:
                new_node = node(current_value, None, None, current_parent, toggle_compare(current_compare))
                current_parent.left = new_node 
                parent_found = True
            else:
                current_parent = current_parent.left
                current_compare = toggle_compare(current_compare)
        else:
            if current_parent.right is None:
                new_node = node(current_value, None, None, current_parent, toggle_compare(current_compare))
                current_parent.right = new_node  
                parent_found = True
            else:
                current_parent = current_parent.right   
                current_compare = toggle_compare(current_compare)

    return root_node

def print_tree(node, indent=0, prefix="root"):
    if indent == 0:
        print()
    if node is not None:
        print(f"{'' if indent == 0 else '|' * indent}" + "--" * indent + f"{'' if indent == 0 else ' '}" + f"{prefix}: ({node.value[0]}, {node.value[1]})")
        print_tree(node.left, indent + 1, "left")
        print_tree(node.right, indent + 1, "right")


input_values = [[3, 6], [17, 15], [13, 15], [6, 12], [9, 1], [2, 7], [10, 19]]
root_node = node(input_values[0], None, None, None, 0)
for i in range(1, len(input_values)):
    root_node = insert_node(input_values[i])
print_tree(root_node)

