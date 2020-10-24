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

    # 定义最终血量的计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    # 三目运算
    print('我赢了') if my_final_hp > enemy_final_hp else print('我输了')

    # 注释快捷键: ctrl+/
    # 复制当前行到下一行：ctrl+d
    # if my_final_hp > enemy_final_hp:
    #     print('我赢了')
    # elif my_final_hp < enemy_final_hp:
    #     print('我输了')
    # else:
    #     print('平局')


fight()