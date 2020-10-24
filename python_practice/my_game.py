# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     my_game
   Description :这是一个回合制游戏，
   Author :       lwy
   date：          2020/10/24
-------------------------------------------------
   Change Activity:
                   2020/10/24:
-------------------------------------------------
"""
import random
import time


class GameRound():
    def __init__(self, my_hp=100, my_power=2, enemy_hp=100, enemy_power=2):
        '''
        初始化
        :param my_hp: 我的血条
        :param my_power: 我的攻击力
        :param enemy_hp: 敌人血条
        :param enemy_power: 敌人攻击力
        '''
        self.my_hp = my_hp
        self.enemy_hp = enemy_hp
        self.my_power = my_power
        self.enemy_power = enemy_power
        self.game_time = 30    # 时间
        self.crit = 0.1    # 暴击率:10%几率双倍伤害
        self.loss_rate = 0.05    # 丢失率:5%几率此次攻击无效
        self.attack_time = 0.5    # 攻击间隔

    def attack(self, hp, power):
        """

        :param hp: 挨打方血量
        :param power: 打人者攻击力
        :return:
        """
        # 这里通过time.sleep()模拟攻击间隔
        time.sleep(self.attack_time)

        msg = ''
        # 攻击是否丢失,如果丢失直接返回hp
        if random.randint(1, 10) == 1:
            msg = '攻击丢失'
            return hp, msg
        else:
            # 攻击是否触发暴击，如果暴击则扣血power*2
            if random.randint(1, 20) == 1:
                hp -= 2*power
                msg = '暴击×2'
            else:
                hp -= power
            return hp, msg

    def round_one(self):
        """
        一轮攻击敌我扣血，并打印出剩余血量
        :return:
        """
        self.my_hp, msg = self.attack(self.my_hp, self.enemy_power)
        print(f'敌人:{msg}')
        self.enemy_hp, msg = self.attack(self.enemy_hp, self.my_power)
        print(f'我的:{msg}')
        print(f'我的剩余血量:{self.my_hp},敌人剩余血量{self.enemy_hp}')

    def start(self):
        """
        开始游戏，血条先为0者败北或是时间结束和剩余血量低者败北
        :return:
        """
        start_time = time.time()
        while True:
            self.round_one()
            # 判断血条是否小于0
            if self.my_hp <= 0:
                print('我输了')
                break
            elif self.enemy_hp <= 0:
                print('我赢了')
                break
            elif time.time() - start_time >= self.game_time:
                if self.my_hp <= self.enemy_hp:
                    print('时间到！')
                    print("""
                    ---------------
                    |   You Lose！ |
                    ---------------""")
                else:
                    print('时间到!')
                    print("""
                    ---------------
                    |   You Win！ |
                    ---------------""")
                break


game_round_one = GameRound()
game_round_one.start()