from Node import Node

"""
Tree
----------

This class represents the Binary Tree used to model our baby mobile.

Each Tree consists of the following properties:
    - root: The root of the Tree

The class also supports the following functions:
    - put(node, child, left_child): Adds child to the given node as the left or right child depending on the value of left_child
    - move_subtree(node_a, node_b, left_child): Move node_a to the left or right child of node_b depending on the value of left_child
    - find_max_imbalance(): Finds the node with the maximum imbalance in the tree

Your task is to complete the following functions which are marked by the TODO comment.
Note that your modifications to the structure of the tree should be correctly updated in the underlying Node class!
You are free to add properties and functions to the class as long as the given signatures remain identical.
"""


class Tree():
    # These are the defined properties as described above
    root: Node

    def __init__(self, root: Node = None) -> None:
        """
        The constructor for the Tree class.
        :param root: The root node of the Tree.
        """
        self.root = root

    def put(self, node: Node, child: Node, left_child: bool) -> None:
        """
        Adds the given child to the given node as the left or right child depending on the value of left_child.
        If a node already has a child at the indicated position, this function should do nothing.
        You are guranteed that the given node is not already part of the tree
        :param node: The node to add the child to.
        :param child: The child to add to the node.
        :param left_child: True if the child should be added to the left child, False otherwise.
        """
        # TODO Add the child to the node as the left or right child depending on the value of left_child
        if left_child is True:
            if node.left_child is None:
                node.left_child=child
                child.parent=node
        else:
            if node.right_child is None:
                node.right_child=child
                child.parent=node
        while node is not None:
            left_weights=0
            if node.left_child is not None:
                left_weights=node.left_child.calculate_weights()
            right_weights=0
            if node.right_child is not None:
                right_weights=node.right_child.calculate_weights()
            node.imbalance=abs(left_weights-right_weights)
            node=node.parent


    def move_subtree(self, node_a: Node, node_b: Node, left_child: bool) -> None:
        """
        Moves the subtree rooted at node_a to the left or right child of node_b depending on the value of left_child.
        If node_b already has a child at the indicated position, this function should do nothing
        You can safely assume that node_b is not descendent of node_a.
        :param node_a: The root of the subtree to move.
        :param node_b: The node to add the subtree to.
        :param left_child: True if the subtree should be added to the left child, False otherwise.
        """

        # TODO Move the subtree rooted at node_a to the left or right child of node_b
        if node_a and node_b:
            parent1 = node_a.parent
            if parent1:
                if parent1.left_child == node_a:
                    parent1.left_child = None
                else:
                    parent1.right_child = None
            self.tree_delete(node_a)
            self.put(node_b, node_a, left_child)
        self.root.update_imbalance()

    def tree_delete(self, node1: Node):
        if node1:
            self.tree_delete(node1.left_child)
            self.tree_delete(node1.right_child)
            del node1

    def treenode_remove(self, node1: Node):
        if self.root:
            # if self.root.left_child and self.root.left_child.is_external():
            if self.root.left_child == node1:
                self.root.left_child = None
            # if self.root.right_child and self.root.right_child.is_external():
            if self.root.right_child == node1:
                self.root.right_child = None
        else:
            return None



    def find_max_imbalance(self) -> int:
        """
        Finds the node with the maximum imbalance in the tree.
        :return: The node with the maximum imbalance.
        """
        nodes = []
        maximum_imbalance = 0
        if self.root is not None:
            nodes.append(self.root)
        while len(nodes) > 0:
            node = nodes.pop(0)
            if node.imbalance > maximum_imbalance:
                maximum_imbalance = node.imbalance
            if node.left_child is not None:
                nodes.append(node.left_child)
            if node.right_child is not None:
                nodes.append(node.right_child)
        return maximum_imbalance


# if __name__ == '__main__':
#     ####################################################
#     A = Node(5)
#     B = Node(10)
#     C = Node(2)
#     D = Node(8)
#     A.add_left_child(C)
#     A.add_right_child(D)
#     C.add_left_child(B)
#     A1 = Tree(A)
#     A1.root.update_imbalance()
#     A1.move_subtree(D, C, False)
#     print('A: ',A1.root.imbalance)
#     print('C: ', A1.root.left_child.imbalance)
#     print('B: ', A1.root.left_child.left_child.imbalance)
#     #########################################################
#     A = Node(10)
#     B = Node(7)
#     C = Node(7)
#     D = Node(7)
#     E = Node(4)
#     F = Node(5)
#     G = Node(6)
#     H = Node(2)
#     C.add_left_child(B)
#     A.add_left_child(C)
#     A.add_right_child(D)
#     D.add_left_child(E)
#     D.add_right_child(F)
#     E.add_left_child(G)
#     E.add_right_child(H)
#
#     A1 = Tree(A)
#     A1.root.update_imbalance()
#
#     print(A1.root.imbalance)
#     print("C:",A1.root.left_child.imbalance)
#     print("D:",A1.root.right_child.imbalance)
#
#     A1.move_subtree(E, B, False)
#     print(A1.root.imbalance)
#     print('C: ',A1.root.left_child.imbalance)
#     #print('C_right: ', A1.root.left_child.right_child.imbalance)
#     print('D:' ,A1.root.right_child.imbalance)
#     print('B:' ,A1.root.left_child.left_child.imbalance)
#     print('E:' ,A1.root.left_child.left_child.right_child.imbalance)
#     print('G:', A1.root.left_child.left_child.right_child.left_child.imbalance)
#     print('H:', A1.root.left_child.left_child.right_child.right_child.imbalance)
#     print('F:', A1.root.left_child.left_child.right_child.left_child.imbalance)
#     # print(A1.root.right_child.left_child.weight)
#
#     print(A1.find_max_imbalance())
