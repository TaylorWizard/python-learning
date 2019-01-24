#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: convert_to_letter_string.py
@time: 1/23/19 6:07 PM
@desc:
"""


class ConvertToLetterString:
    @staticmethod
    def convert(chars):
        if chars is None or len(chars) == 0:
            return

        chars_list = list(chars)
        return ConvertToLetterString.process(chars_list, 0)

    @staticmethod
    def process(chars, i):
        if i == len(chars):
            return 1

        if chars[i] == '0':
            return 0

        if chars[i] == '1':
            res = ConvertToLetterString.process(chars, i + 1)
            if i + 1 < len(chars):
                res += ConvertToLetterString.process(chars, i + 2)
            return res

        if chars[i] == '2':
            res = ConvertToLetterString.process(chars, i + 1)
            if i + 1 < len(chars) and ('0' < chars[i] <= '6'):
                res += ConvertToLetterString.process(chars, i + 2)
            return res

        return ConvertToLetterString.process(chars, i + 1)


if __name__ == '__main__':
    print(ConvertToLetterString.convert('11111'))

