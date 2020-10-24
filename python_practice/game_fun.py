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
import random


# 定义fight函数
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200

    # 打印敌人的血量和攻击力
    print(f'敌人的血量为{enemy_hp}, 攻击力为{enemy_power}')

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp -= enemy_power
        enemy_hp -= my_hp

        # 判断谁的血量小于等于0
        if my_hp <= 0:
            # 打印我和敌人的剩余血量
            print(f'我的剩余血量为{my_hp}')
            print(f'敌人的剩余血量为{enemy_hp}')
            print('我输了')
            # 满足条件跳出循环
            break
        elif enemy_hp <= 0:
            print(f'我的剩余血量为{my_hp}')
            print(f'敌人的剩余血量为{enemy_hp}')
            print('我赢了')
            break


if __name__ == '__main__':
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # 让敌人的hp从hp列表中随机挑选一个值
    enemy_hp = random.choice(hp)

    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(190, 210)

fight()