class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node {self.id_node}, leftchild {self.left}, rightchild {self.right}'

    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node)
        if self.right:
            self.right.print_tree()

    def append_new_nodes(self, nodes):
        tree_list = []
        duplicates = []
        tree_list.append(self.id_node)
        for i in nodes:
            if i not in tree_list:
                tree_list.append(i)
                self.insert(i)
            else:
                duplicates.append(i)
        if len(duplicates) != 0:
            print("Duplicated nodes have not been added to the tree:", *duplicates)

    def min_node(self):
        if self.left is None:
            return self.id_node
        return self.left.min_node()

    def max_node(self):
        if self.right is None:
            return self.id_node
        return self.right.max_node()

    def node_delete(self, root, key):
        if root is None:
            return root
        if key < root.id_node:
            root.left = self.node_delete(root.left, key)
        elif key > root.id_node:
            root.right = self.node_delete(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            if root.left and root.right:
                temp = root.right
                root.id_node = temp.id_node
                root.right = self.node_delete(root.right, root.id_node)
        return root


root_node = Tree(13)
nodes = [1, 2, 3, 15, 13, 8, 7, 8, 2, 10, 1]
root_node.append_new_nodes(nodes)
print("Tree after list appending:")
root_node.print_tree()

print("Minimal =", root_node.min_node())
print("Maximal =", root_node.max_node())

root_node.node_delete(root_node, 13)
print("Tree after node deletion:")
root_node.print_tree()