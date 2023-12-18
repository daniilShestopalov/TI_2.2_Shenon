import graphviz

def visualize_tree(node):
    dot = graphviz.Digraph()
    code_dict = generate_codes(node)

    def traverse(n, parent_name=None, edge_label=None):
        if len(n.symbols) == 1:
            name = n.symbols[0] + " (" + code_dict[n.symbols[0]] + ")"
        else:
            name = ','.join(n.symbols)
        total_prob = sum(n.probabilities)
        dot.node(name, label=f"{name}\n{[p for p in n.probabilities]}\nTotal: {total_prob}")
        if parent_name:
            dot.edge(parent_name, name, label=edge_label)
        if n.left:
            traverse(n.left, name, "0")
        if n.right:
            traverse(n.right, name, "1")

    traverse(node)
    return dot

def generate_codes(node, current_code="", code_dict={}):
    if not node.left and not node.right:  # If it's a leaf node
        assert len(node.symbols) == 1
        code_dict[node.symbols[0]] = current_code
    if node.left:
        generate_codes(node.left, current_code + "0", code_dict)
    if node.right:
        generate_codes(node.right, current_code + "1", code_dict)
    return code_dict