class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata


class Tree:
    def __init__(self):
        self.root = None


def build_tree(nodes):
    def build(nodes):
        children_num = nodes[0]
        metadata_num = nodes[1]
        length = 2
        children = []

        for _ in range(children_num):
            child_len, child = build(nodes[length:])
            children.append(child)
            length += child_len

        return length + metadata_num, Node(children, nodes[length:length + metadata_num])

    tree = Tree()
    tree.root = build(nodes)[1]
    return tree


def count_metadata_sum(nodes):
    tree = build_tree(nodes)

    def traverse(node):
        return sum(node.metadata) + sum(traverse(child) for child in node.children)

    return traverse(tree.root)


if __name__ == "__main__":
    with open('day08/input.txt') as inp:
        data = list(map(int, inp.read().strip().split(' ')))

    print(count_metadata_sum(data))  # 44838
