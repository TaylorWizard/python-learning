#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: my_sets.py
@time: 1/17/19 4:05 PM
@desc: 自定义为kruskal算法使用的set类, 使用了hash map 和 set
        1. 创建一个 hash map 存放 每个顶点所在的集合
        2. 创建一个 set, 存放着在同一个集合的所有顶点
        3. 每个顶点最开始都独立是一个集合, 将每个顶点加入到不同的集合中去
        4. MySets 提供 isSameSet, 判断两个顶点是否在一个集合里
        5. MySets 提供 mergeSet, 将两个集合合并
"""


class MySets:
    def __init__(self, n_list):
        self.node_find_set_map = dict()
        for node in n_list[0:]:
            s = set()
            s.add(node)
            # 存放结构为{当前结点: 所在的集合}
            self.node_find_set_map.update({node: s})

    def is_same_set(self, a, b):
        return self.node_find_set_map.get(a) == self.node_find_set_map.get(b)

    def union(self, a, b):
        set_a = self.node_find_set_map.get(a)
        set_b = self.node_find_set_map.get(b)
        for cur in set_b:
            set_a.add(cur)
            self.node_find_set_map.update({cur: set_a})


if __name__ == '__main__':
    pass
