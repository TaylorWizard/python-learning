#!/usr/bin/env python
# encoding: utf-8
"""
@author: Gakki
@software: garner
@file: best_arrangement.py
@time: 1/20/19 9:01 PM
@desc:
"""
from operator import attrgetter
import time
import random


class Program:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class BestArrangement:
    def __init__(self):
        pass

    @staticmethod
    def best_arrangement(programs, start):
        p_list = sorted(programs, key=lambda program: program.end)
        print([(p.start, time.strftime('%y-%m-%d %H %M %S', time.localtime(p.end))) for p in p_list[0:]])
        result = 0
        for p in p_list[0:]:
            if start < p.start:
                print('能够被安排的会议的开始时间: {0}'.format(time.strftime('%y-%m-%d %H:%M:%S', time.localtime(p.start))),
                      '结束时间: {0}'.format(time.strftime('%y-%m-%d %H:%M:%S', time.localtime(p.end))))
                result += 1
                start = p.end

        return result


if __name__ == '__main__':
    program_list = [
        Program(
            time.mktime((2018, 12, 31, 9, 20, 0, 0, 0, 0)),
            time.mktime((2018, 12, 31, 9, 55, 0, 0, 0, 0))
        ),
        Program(
            time.mktime((2018, 12, 31, 9, 30, 0, 0, 0, 0)),
            time.mktime((2018, 12, 31, 10, 30, 0, 0, 0, 0))
        ),
        Program(
            time.mktime((2018, 12, 31, 9, 40, 0, 0, 0, 0)),
            time.mktime((2018, 12, 31, 10, 5, 0, 0, 0, 0))
        ),
        Program(
            time.mktime((2018, 12, 31, 9, 30, 0, 0, 0, 0)),
            time.mktime((2018, 12, 31, 11, 55, 0, 0, 0, 0))
        ),
        Program(
            time.mktime((2018, 12, 31, 11, 5, 0, 0, 0, 0)),
            time.mktime((2018, 12, 31, 11, 35, 0, 0, 0, 0))
        ),
    ]
    s_time = time.mktime((2018, 12, 31, 9, 20, 0, 0, 0, 0))
    print(BestArrangement.best_arrangement(program_list, s_time))
