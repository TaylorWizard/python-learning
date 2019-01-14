from tree.bst import BST, Node
import sys


class ReturnType:
    def __init__(self, is_bst, min_value, max_value):
        self.isBST = is_bst
        self.min = min_value
        self.max = max_value


class IsBST:
    def __init__(self):
        pass

    @staticmethod
    def is_bst(node):
        return IsBST.process(node).isBST

    @staticmethod
    def process(node):
        """

        返回是否为bst
        :param node:
        :return:
        """
        if node is None:
            return ReturnType(True, sys.maxsize, -sys.maxsize)

        left_data = IsBST.process(node.left)
        right_data = IsBST.process(node.right)

        v_min = min(node.data, min(left_data.min, right_data.min))
        v_max = max(node.data, max(left_data.max, left_data.max))

        is_bst = left_data.max < node.data \
            and left_data.isBST \
            and right_data.min > node.data \
            and right_data.isBST

        return ReturnType(is_bst, v_min, v_max)


if __name__ == '__main__':
    node_lyst = [17, 5, 35, 2, 11, 29, 38, 10, 12]
    bst = BST(node_lyst)
    result = IsBST.is_bst(bst.get_root())
    print(result)
    flag, n, p = bst.search(bst.get_root(), bst.get_root(), 38)
    print('=========================================')

    node = Node(10)
    node.left = Node(15)
    node.right = Node(5)
    node.left.left = Node(28)
    result_2 = IsBST.is_bst(node)
    print(result_2)