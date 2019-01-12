from tree.bst import BST
from queue import Queue


class TreeMaxWidth:
    def __init__(self):
        pass

    @staticmethod
    def get_max_width(root):
        cur_level = 0
        max_width = 0
        cur_width = 0
        level_map = {}
        _queue = Queue()

        level_map[root] = 1
        _queue.put(root)

        node = None
        left = None
        right = None

        #

        while not _queue.empty():
            node = _queue.get()
            left = node.left
            right = node.right

            if left is not None:
                level_map[left] = level_map[node] + 1
                _queue.put(left)
            if right is not None:
                level_map[right] = level_map[node] + 1
                _queue.put(right)

            if level_map[node] > cur_level:
                cur_level = level_map[node]
                cur_width = 1
            else:
                cur_width += 1

            max_width = max(cur_width, max_width)

        return max_width

if __name__ == '__main__':
    node_list = [17, 5, 35, 2, 11, 29, 38]
    tree_max_width = TreeMaxWidth()
    bst_tree = BST(node_list)
    width = tree_max_width.get_max_width(bst_tree.get_root())
    print(width)