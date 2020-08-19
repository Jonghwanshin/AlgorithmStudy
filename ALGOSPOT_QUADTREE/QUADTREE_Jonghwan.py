#!/usr/bin/env python3

class QuadTree:

    def __init__(self, value='', parent_node=None):
        self.value = value
        self.parent = parent_node
        self.children = []

    def is_no_child(self):
        return len(self.children) == 0

    def flip(self):
        if not self.is_no_child():
            self.children[0], self.children[2] = self.children[2], self.children[0]
            self.children[1], self.children[3] = self.children[3], self.children[1]
            for ch in self.children:
                ch.flip()

    def to_string(self, output_str):
        output_str += self.value
        if not self.is_no_child():
            for ch in self.children:
                output_str = ch.to_string(output_str)
        return output_str

    def from_string(self, pos, str_input):
        while (len(self.children)<4) and pos < len(str_input):
            s = str_input[pos]
            new_node = QuadTree(s, self)
            self.children.append(new_node)
            if s == 'x':
                pos = new_node.from_string(pos+1, str_input)
            else:
                pos = pos + 1
        return pos

    def import_string(self, str_input):
        pos = 0
        while pos < len(str_input):
            if pos == 0:
                self.value = str_input[pos]
                pos += 1
            else:
                pos = self.from_string(pos, str_input)


def main():
    nd = input().split()
    num_inputs = nd[0]
    trees = []
    for num in range(int(num_inputs)):
        str_quad_tree = input().split()[0]
        tree = QuadTree()
        tree.import_string(str_quad_tree)
        trees.append(tree)
    for tree in trees:
        tree.flip()
        print(tree.to_string(''))


if __name__ == '__main__':
    main()
