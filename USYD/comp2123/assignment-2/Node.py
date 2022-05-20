"""
Binary Tree Node
----------

This class represents an individual Node in a Binary Tree.

Each Node consists of the following properties:
    - left_child: Pointer to the left child of the Node
    - right_child: Pointer to the right child of the Node
    - parent: Pointer to the parent of the Node
    - weight: The weight of the Node
    - imbalance: The imbalance of the Node (absolute difference between the weight of the left and right subtree)

The class also supports the following functions:
    - add_left_child(Node): Adds the given Node as the left child
    - add_right_child(Node): Adds the given Node as the right child
    - is_external(): Returns True if the Node is a leaf node
    - update_weight(int): Updates the weight of the Node
    - get_left_child(): Returns the left child of the Node
    - get_right_child(): Returns the right child of the Node
    - get_imbalance(): Returns the imbalance of the Node

Your task is to complete the following functions which are marked by the TODO comment.
Note that your Node should automatically update the imbalance as nodes are added and weights are updated!
You are free to add properties and functions to the class as long as the given signatures remain identical
"""


class Node():
    # These are the defined properties as described above
    left_child: 'Node'
    right_child: 'Node'
    parent: 'Node'
    weight: int
    imbalance: int

    def __init__(self, weight: int) -> None:
        """
        The constructor for the Node class.
        :param weight: The weight of the node.
        """

        # TODO Initialize the properties of the node
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.weight = weight
        self.imbalance = 0

    def root_node(self):
        if not self.parent:
            return self
        return self.parent.root_node()

    def add_left_child(self, node: 'Node') -> None:
        """
        Adds the given node as the left child of the current node.
        Should do nothing if the the current node already has a left child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the left child.
        """

        # TODO Add the given node as the left child of the current node
        if not self.left_child and node!=None:
            self.left_child = node
            node.parent = self
            root_node=self.root_node()
            root_node.update_imbalance()

    def add_right_child(self, node: 'Node') -> None:
        """
        Adds the given node as the right child of the current node.
        Should do nothing if the the current node already has a right child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the right child.
        """

        # TODO Add the given node as the right child of the current node
        if not self.right_child and node!=None:
            self.right_child = node
            node.parent = self
            root_node = self.root_node()
            root_node.update_imbalance()

    def is_external(self) -> bool:
        """
        Returns True if the node is a leaf node.
        :return: True if the node is a leaf node.
        """

        return self.left_child is None and self.right_child is None

    def update_weight(self, weight: int) -> None:
        """
        Updates the weight of the current node.
        :param weight: The new weight of the node.
        """

        # TODO Update the weight of the node
        self.weight = weight
        root_node=self.root_node()
        root_node.update_imbalance()


    def get_left_child(self) -> 'Node':
        """
        Returns the left child of the current node.
        :return: The left child of the current node.
        """

        return self.left_child

    def get_right_child(self) -> 'Node':
        """
        Returns the right child of the current node.
        :return: The right child of the current node.
        """

        return self.right_child


    def get_imbalance(self):
        return self.imbalance

    def calculate_weights(self)->int:
        weights=self.weight
        if not self.left_child:
            weights+=self.left_child.calculate_weights()
        if not self.right_child :
            weights+=self.right_child.calculate_weights()
        return weights

    def update_imbalance(self):
        left_weights= 0
        if self.left_child is not None:
            left_weights=self.left_child.calculate_weights()
        right_weights=0
        if self.right_child is not None:
            right_weights=self.right_child.calculate_weights()
        self.imbalance=abs(left_weights-right_weights)
        if self.left_child:
            self.left_child.update_imbalance()
        if self.right_child:
            self.right_child.update_imbalance()
