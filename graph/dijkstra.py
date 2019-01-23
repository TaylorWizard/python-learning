#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: dijkstra.py
@time: 1/18/19 1:36 PM
@desc: 1. 创建一个distance map 存放从指定点到某个顶点的距离
       2. 创建一个selected mao 存放已经被选择过的顶点, 如果
          某个顶点没有被放入这个map，就会计算出从出发点到该顶点的最小距离,
       3. 最开始出发点到所有点的距离看作是正无穷大, 直到一个点被选择才会解
          锁相应边以及能够到达的点, 并且才能拿到每个边的权重, 来计算出出发点到
          能够到达点的最小权重
       4. 一旦有新的点被选择, 就会有新的边被解锁, 可能出发点到某个顶点的距离最小值
          会变小, 这里就必须重新计算
       4. 首先从出发点开始, 将自己加入到distance map里, 并且设置到自己的距离为0
       5. 遍历当前选择点的所有与它相连的边, 第一次是出发点, 找到某个边的to节点
"""
import sys
from graph.graph_generator import GraphClass


class Dijkstra:
    def __init__(self):
        pass

    @staticmethod
    def dijkstra_1(head):
        """
        不用堆结构的dijkstra
        :param head: 传入图的出发点
        :return: 返回distance map，{node, distance} key: 顶点, value:出发点到该顶点的距离
        """
        distance_map = {}
        selected_node = set()

        distance_map.update({head: 0})
        min_node = Dijkstra.get_min_distance_and_unselected_node(distance_map, selected_node)
        while min_node is not None:
            distance = distance_map.get(min_node)
            for edge in min_node.l_edge[0:]:
                to_node = edge.get_to()  # 获取当前边的to节点
                if to_node not in distance_map:
                    distance_map.update({to_node: distance + edge.get_weight()})
                distance_map.update({to_node: min(distance_map.get(to_node), distance + edge.get_weight())})
            selected_node.add(min_node)
            min_node = Dijkstra.get_min_distance_and_unselected_node(distance_map, selected_node)

        return distance_map

    @staticmethod
    def get_min_distance_and_unselected_node(d_map, s_node):
        """
        找出当前没有被选择过的顶点, 并且所有没有被选择顶点与出发点的距离, 选择出最小的返回
        :param d_map: distance map
        :param s_node: selected node
        :return:
        """
        min_distance = sys.maxsize
        min_node = None
        for entry in d_map.items():
            n = entry[0]
            distance = entry[1]
            if n not in s_node and distance < min_distance:
                min_node = n
                min_distance = distance

        return min_node


if __name__ == '__main__':
    g_matrix = [
        [10, 5, 3],  # [weight, from, to]
        [9, 5, 4],
        [2, 6, 4],
        [5, 4, 3],
        [11, 5, 6],
        [6, 3, 1],
        [18, 1, 2],
    ]

    g = GraphClass.graph_generator(g_matrix)
    dis_map = Dijkstra.dijkstra_1(g.nodes.get(5))
    for node, value in dis_map.items():
        print('5 -> {0}'.format(node.value), 'distance: {dis}'.format(dis=value))
