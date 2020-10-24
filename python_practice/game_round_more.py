# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     game_round1
   Description :
   Author :       lwy
   date：          2020/10/24
-------------------------------------------------
   Change Activity:
                   2020/10/24:
-------------------------------------------------
"""

"""
一个回合制游戏，每一个角色都有hp和power，hp代表血量，power代表攻击力，
hp初始值为1000，power的初始值为200.
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""


# 定义fight函数
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp -= enemy_power
        enemy_hp -= my_hp

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            print('我输了')
        elif enemy_hp <= 0:
            print('我赢了')
            break


fight()