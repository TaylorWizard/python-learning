#!/usr/bin/env python
# encoding: utf-8
"""
@author: huangjing
@software: garner
@file: graph-generator.py
@time: 1/16/19 2:40 PM
@desc:
"""


class GraphClass:
    class Edge:
        """

        图的边的类表示
        """
        def __init__(self, _weight, _from, _to):
            self._weight = _weight
            self._from = _from
            self._to = _to

    class Node:
        """

        图的顶点类定义
        """
        def __init__(self, value):
            self.value = value
            self.in_degree = 0  # 出度: 有多少顶点直接指向自己
            self.out_degree = 0  # 入度: 自己直接指向了多少个顶点
            self.l_next = []  # 从自己出发, 自己指向了哪些顶点, 用一个列表存放
            self.l_edge = []  # 自己有哪些边

    class Graph:
        def __init(self):
            self.nodes = {}
            self.edges = set()

    @staticmethod
    def graph_generator(matrix):
        """

        :param matrix: 1、代表图中所有的边
                       2、是一个 N*3 的矩阵, N条边
                       3、每条边是一个小数组[weight, from, to] weight: 边的权重 from: 起始顶点 to: 结束结点
        :return:
        """
        graph = GraphClass.Graph()
        #  如果graph图类没有from或to顶点信息, 将from 或 to 添加进graph
        #  生成一个新的from和to的node
        #  生成一个新的from 到 to 的 edge
        #  from顶点的出度 + 1, to顶点的入度 + 1
        #  from顶点的l_next数组添加生成的新的edge, graph添加新的edge
        for i in range(0, len(matrix)):
            _weight = matrix[i][0]
            _from = matrix[i][1]
            _to = matrix[i][2]

            if _from not in graph.nodes:
                graph.nodes.update({_from: GraphClass.Node(_from)})
            if _to not in graph.nodes:
                graph.nodes.update({_to: GraphClass.Node(_to)})

            from_node = GraphClass.Node(_from)
            to_node = GraphClass.Node(_to)

            from_node.l_next.append(to_node)
            from_node.out_degree += 1

            to_node.in_degree += 1

            new_edge = GraphClass.Edge(_weight, from_node, to_node)
            from_node.l_edge.append(new_edge)
            graph.edges.add(new_edge)

        return graph


if __name__ == '__main__':
    pass
