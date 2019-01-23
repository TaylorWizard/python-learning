#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: trie.py
@time: 1/19/19 2:08 PM
@desc:
"""


class TrieNode:
    def __init__(self):
        self.__pass = 0
        self.__end = 0
        self.__next = list([None for i in range(0, 26)])

    def add_pass(self):
        self.__pass += 1

    def add_end(self):
        self.__end += 1

    def minus_pass(self):
        if self.__pass > 0:
            self.__pass -= 1

    def minus_end(self):
        if self.__end > 0:
            self.__end -= 1

    def set_next(self, index, v):
        if index > len(self.__next) - 1:
            return
        self.__next[index] = v

    def get_end(self):
        return self.__end

    def get_pass(self):
        return self.__pass

    def get_next(self):
        return self.__next


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        char_list = list(word)

        for v in char_list[0:]:
            index = ord(v) - ord('a')
            if node.get_next()[index] is None:
                node.set_next(index, TrieNode())
            node = node.get_next()[index]
            node.add_pass()
        node.add_end()

    def delete(self, word):
        if self.search(word) != 0:
            node = self.root
            char_list = list(word)
            for v in char_list[0:]:
                index = ord(v) - ord('a')
                if node.get_next()[index].minus_pass() == 0:
                    node.get_next()[index] = None
                node = node.get_next()[index]

            return node.minus_end()

    def search(self, word):
        if word is None:
            return 0
        char_list = list(word)
        node = self.root

        for v in char_list[0:]:
            index = ord(v) - ord('a')
            if node.get_next()[index] is None:
                return 0
            node = node.get_next()[index]

        return node.get_end()

    def prefix_num(self, prefix):
        if prefix is None:
            return 0
        char_list = list(prefix)
        node = self.root
        print(char_list)
        for v in char_list[0:]:
            index = ord(v) - ord('a')
            if node.get_next()[index] is None:
                return 0
            node = node.get_next()[index]

        return node.get_pass()


if __name__ == '__main__':
    str_list = ['abc', 'bcd', 'def', 'efg', 'abcde', 'ab']
    trie = Trie()
    for value in str_list[0:]:
        trie.insert(value)
    trie.insert('abc')  # 2
    trie.insert('abc')  # 3
    trie.insert('abc')  # 4
    trie.insert('abcde')  # 2
    print(trie.prefix_num('ef'))  # 1
    print(trie.search('abcde'))  # 2
    trie.delete('abc')  # -1
    print(trie.search('abc'))  # 3
