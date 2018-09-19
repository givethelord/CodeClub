#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/3/25 16:53
# @Author  : Administrator
# @Site    : 
# @File    : 2048.py
# @Software: PyCharm

"""
-----------------------------------------------------
Function:
200行Python代码实现2048

来源: 实验楼
链接: https://www.shiyanlou.com/courses/368/labs/1172/document


-----------------------------------------------------
"""
import curses
from random import randrange,choice
from collections import defaultdict

import sys
if sys.version_info < (3, 4):
    raise RuntimeError('At least Python 3.4 is required')

action = ['Up','Left','Down','Right','Restart','Exit']

letter_code = [ord(ch) for ch in 'WAXDRQwaxdrq']

acitons_dict = dict(zip(letter_code,action * 2))


def main(stdscr):

    def init():
        #重置游戏棋盘
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #画出当前棋盘状态
        #读取用户输入得到action
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        #if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'

    #状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()
