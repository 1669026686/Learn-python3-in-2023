# -*- coding: utf-8 -*-
# @date 2022/12/31 15:29
# @Author Ambition
# @FileName 221231_game.py
# @Software PyCharm
"""用python设计第一个游戏"""
temp = input("不妨猜一下我现在心里想的是什么数字：")
guess = int(temp)

if guess == 8:
    print("你是我肚子里的蛔虫吗？牛牛牛")
    print("哼！猜中了也没有奖励！")
else:
    print("猜错啦，小甲鱼心里想的是8！")
print("游戏结束，不玩啦！")
