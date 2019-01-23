#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: reverse_stack_using_recursive.py
@time: 1/23/19 5:43 PM
@desc:
"""
from queue import LifoQueue


class ReverseStackUsingRecursive:
    @staticmethod
    def reverse(stack):
        if stack.empty():
            return

        i = ReverseStackUsingRecursive.f(stack)
        ReverseStackUsingRecursive.reverse(stack)
        stack.put(i)

    @staticmethod
    def f(stack):
        """
        得到并且移除栈底的元素
        :param stack:
        :return:
        """
        result = stack.get()
        if stack.empty():
            return result
        else:
            last = ReverseStackUsingRecursive.f(stack)
            stack.put(result)
            return last


if __name__ == '__main__':
    queue = LifoQueue()
    queue.put(4)
    queue.put(3)
    queue.put(2)
    queue.put(1)
    while not queue.empty():
        print(queue.get())
    print('===============')
    queue.put(4)
    queue.put(3)
    queue.put(2)
    queue.put(1)
    ReverseStackUsingRecursive.reverse(queue)
    while not queue.empty():
        print(queue.get())
