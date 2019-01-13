from tree.bst import BST
from queue import LifoQueue

class DFS:
    def __init__(self):
        pass

    @staticmethod
    def depth_first_search(root):

        if root is None:
            return None

        stack = LifoQueue()
        stack.put(root)
        level_map = dict()
        cur_depth = 0 # 当前的第几层

        level_map[root] = 1

        while not stack.empty():
            node = stack.get()
            print(node.data, end=' ')

            if node.right is not None:
                stack.put(node.right)
                level_map[node.right] = level_map[node] + 1
            if node.left is not None:
                stack.put(node.left)
                level_map[node.left] = level_map[node] + 1

            if level_map[node] > cur_depth:
                cur_depth += 1
        print()

        return cur_depth

if __name__ == '__main__':
    node_list = [17, 5, 35, 2, 11, 29, 38, 37, 40]
    bst_tree = BST(node_list)
    depth = DFS.depth_first_search(bst_tree.get_root())
    print(depth)