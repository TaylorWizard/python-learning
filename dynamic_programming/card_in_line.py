#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: card_in_line.py
@time: 1/23/19 1:40 PM
@desc: 给定一个整型数组arr，代表数值不同的纸牌排成一条线。玩家A和玩家B依次拿走每张纸牌，
       规定玩家A先拿，玩家B后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家A 和玩家B都绝顶聪明。请返回最后获胜者的分数。
      【举例】
       arr=[1,2,100,4]。 开始时，玩家A只能拿走1或4。如果开始时玩家A拿走1，则排列变为[2,100,4]，接下来 玩家 B可以拿走
       2或4，然后继续轮到玩家A... 如果开始时玩家A拿走4，则排列变为[1,2,100]，接下来玩家B可以拿走1或100，然后继 续轮到玩
       家A... 玩家A作为绝顶聪明的人不会先拿4，因为拿4之后，玩家B将拿走100。所以玩家A会先拿1， 让排列变为[2,100,4]，接下来
       玩家B不管怎么选，100都会被玩家 A拿走。玩家A会获胜， 分数为101。所以返回101。
       arr=[1,100,2]。 开始时，玩家A不管拿1还是2，玩家B作为绝顶聪明的人，都会把100拿走。玩家B会获胜,分数为100。所以返回100。
"""


class CardInLine:
    def __init__(self):
        pass

    @staticmethod
    def win_1(card_list):
        """
        选择拿牌分先手和后手
        如果在L到R的范围上, 先手拿牌, 先拿L, 那么后手我就在L + 1到 R 范围上拿
        如果先拿R, 那么后手我就在L到R-1的范围上后拿
        就会出现上述两种情况, 两种都去尝试, 取最大值
        如果在L在R的范围上后手拿, 对方先拿L, 能拿的只有L+1到R上的牌, 对方先拿R，能拿的只有L到R-1上的牌
        :param card_list:
        :return:
        """
        if card_list is None or len(card_list) == 0:
            return 0

        return max(CardInLine.f(card_list, 0, len(card_list) - 1),
                   CardInLine.s(card_list, 0, len(card_list) - 1))

    @staticmethod
    def f(card_list, i, j):
        if i == j:
            return card_list[i]

        return max(card_list[i] + CardInLine.s(card_list, i + 1, j),
                   card_list[j] + CardInLine.s(card_list, i, j - 1))

    @staticmethod
    def s(card_list, i, j):
        if i == j:
            return 0

        return min(CardInLine.f(card_list, i + 1, j), CardInLine.f(card_list, i, j - 1))


if __name__ == '__main__':
    card = [1, 4, 5, 3, 4, 5, 2, 1]
    win_points = CardInLine.win_1(card)
    print(win_points)
