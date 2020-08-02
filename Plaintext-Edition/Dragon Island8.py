# -*- coding:utf-8 -*-
# 正式发布版本
#Dragon Island 1  v0.5.0

from abc import ABC, abstractmethod
import random
import sys
import time
import math

land_list = ['宝库', '草地', '高山', '池塘边', '火山', '黑森林', '森林',
             '废墟', '神殿', '沙漠', '沼泽', '矿洞', '小岛', '草地', '高山', '池塘边', '火山', '黑森林', '森林',
             '废墟', '神殿', '沙漠', '沼泽', '矿洞', '小岛']  # 创立一个地点列表备用
# npc_list = ['一条幼年白龙', '一个哥布林', '一个巨人', '一个机器人', '一个骷髅','一个僵尸','一朵曼陀罗花']  # 创建一个人物列表备用

# 怪兽和角色的基础类


class Creature(ABC):
    AC = 0  # 防御力
    AB = 0  # 攻击加成
    HP = 0  # 生命值
    QB = 0  # 灵敏值
    Bag = []  # 背包
    Name = 'Unknown'

    @abstractmethod
    def get_status_str(self):  # 状态字符串
        raise NotImplementedError()

    @abstractmethod
    def do_fight_round(self, opponent):
        raise NotImplementedError()

    def is_alive(self):  # 存活确认
        return self.AC > 0 and self.AB > 0 and self.HP > 0 and self.QB > 0

    def judge(self, diff):  # 根据QB差值，判断攻击等技能是否成立
        threshhold = 0
        if diff >= 0:
            threshhold = 1 - math.pow(0.5, diff)
        else:
            threshhold = math.pow(0.5, -diff)

        return random.random() < threshhold

# 怪兽的基础类


class Monster(Creature):
    Money = 10

    def get_status_str(self):
        return f'AC: {self.AC}, AB: {self.AB}, HP: {self.HP}, QB: {self.QB}'


# 网游职业的基础类
class Role(Creature):
    attack_results = ['它攻击了你！你受伤了！', '你杀死了它！你赢了！',
                      '你杀死了它！你赢了！', '你杀死了它！你赢了！', '你杀死了它！你赢了！']
    escape_results = ['它没有看到你的离开！你安然无恙！', '它攻击了你！你受伤了！',
                      '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', ]
    hide_results = ['你没躲过它的攻击！你受伤了！', '它没有发现你，你成功逃过一劫！',
                    '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！']

    def __init__(self):
        self.Money = 100
        #self.total_rounds = 0
        self.introduce = [f'你选择了{self.Name}！\n这是一个不错的职业，只是…\n你首先要了解：\n我们的世界由五大属性组成：',
                          '分别是：\n防御值（AC）：在你遭受攻击时挡住攻击',
                          '生命值（HP）：在你受到攻击时遭受的伤害',
                          '攻击加值（AB）：在你挥出巨剑时带给敌方的痛苦感受',
                          '灵敏值（QB）：在你躲过敌方致命一击时的冲刺',
                          '与金钱（Money）：你胜利击退可恶的铁脑壳时获取的奖赏',
                          f'当你了解了这些之后，你需要知道{self.Name}的各项属性：\n AC = {self.AC}  HP ={self.HP}  AB = {self.AB}  QB ={self.QB}  Money = {self.Money}\n(任何一项为0，你都会死亡(除Money之外))']

    def display_role_introduce(self):
        for line in self.introduce:
            print(line)
            time.sleep(1)

    def get_status_str(self):
        return f'AC: {self.AC}, AB: {self.AB}, HP: {self.HP}, QB: {self.QB}, Money: {self.Money}'

# 幼年黑龙 lv.4 强者 伏兵


class Monster_YoungBlackDragon(Monster):
    def __init__(self):
        self.AC = 18
        self.HP = 22
        self.AB = 14
        self.QB = 10
        self.Name = '幼年黑龙'
        self.Money = random.randint(25, 65)

    def do_fight_round(self, role):
        print('幼年黑龙对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了幼年黑龙的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('幼年黑龙使用了啮咬攻击！')
                self.AB -= 2
                self.AC -= 1
                if self.judge(-2):
                    print('幼年黑龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)
                    print('幼年黑龙对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('幼年黑龙使用了龙怒攻击！')
                self.HP -= 1
                self.AC -= 1
                if self.judge(-2):
                    print('幼年黑龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 6)
                    print('幼年黑龙对你造成了物理伤害！')
            else:
                print('幼年黑龙使用了龙息攻击')
                self.AC -= 3
                self.QB -= 1
                self.AB -= 2
                if self.judge(-2):
                    print('幼年黑龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(6, 8)
                    print('幼年黑龙对你造成了强酸伤害！')
# 幼年白龙 lv.3 强者 蛮战


class Monster_YoungWhiteDragon(Monster):
    def __init__(self):
        self.AC = 17
        self.HP = 20
        self.AB = 13
        self.QB = 8
        self.Name = '幼年白龙'
        self.Money = random.randint(20, 60)

    def do_fight_round(self, role):
        print('幼年白龙对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了幼年白龙的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('幼年白龙使用了啮咬攻击！')
                self.AB -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('幼年白龙的攻击失败了！你没有受到伤害')

# 地精剑士 lv.1 杂兵


class Monster_GoblinCutter(Monster):
    def __init__(self):
        self.AC = 8
        self.HP = 3
        self.AB = 7
        self.QB = 10
        self.Name = '地精剑士'
        self.Money = random.randint(1, 50)

    def do_fight_round(self, role):
        print('地精剑士对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了地精剑士的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('地精剑士使用了空裂斩！')
                self.AB -= 1
                self.AC -= 1
                if self.judge(-1.5):
                    print('地精剑士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(1, 3)
                    print('地精剑士对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('地精剑士使用了短剑快刺！')
                self.QB -= 2
                self.AC -= 1
                if self.judge(-1.5):
                    print('地精剑士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(1, 3)
                    print('地精剑士对你造成了物理伤害！')
            else:
                print('地精剑士使用了地精战术')
                self.AC -= 1
                self.QB -= 3
                self.AB -= 1
                if self.judge(-1.25):
                    print('地精剑士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 4)
                    print('地精剑士对你造成了物理伤害！')

# 地精巫师 lv.3 控制（头目）


class Monster_GoblinHexer(Monster):
    def __init__(self):
        self.AC = 9
        self.HP = 12
        self.AB = 8
        self.QB = 10
        self.Name = '地精巫师'
        self.Money = random.randint(20, 60)

    def do_fight_round(self, role):
        print('地精巫师对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了地精巫师的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('地精巫师使用了目盲术！')
                self.HP -= 1
                self.AC -= 1
                if self.judge(-2):
                    print('地精巫师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)
                    print('地精巫师对你造成了法术伤害！')
            elif how_to_fight <= 8:
                print('地精巫师使用了刺击术！')
                self.QB -= 2
                self.HP -= 1
                if self.judge(-2):
                    print('地精巫师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)
                    print('地精巫师对你造成了法术伤害！')
            else:
                print('地精巫师使用了困扰之云')
                self.HP -= 2
                self.QB -= 2
                self.AB -= 1
                if self.judge(-2):
                    print('地精巫师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)
                    print('地精巫师对你造成了范围性法术伤害！')

# 朽坏骷髅 lv.1 杂兵


class Monster_DecrepitSkeleton(Monster):
    def __init__(self):
        self.AC = 7
        self.HP = 3
        self.AB = 8
        self.QB = 9
        self.Name = '朽坏骷髅'
        self.Money = random.randint(1, 50)

    def do_fight_round(self, role):
        print('朽坏骷髅对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了朽坏骷髅的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('朽坏骷髅使用了腐化之箭！')
                self.QB -= 1
                if self.judge(-1.5):
                    print('朽坏骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(1, 2)
                    print('朽坏骷髅对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('朽坏骷髅使用了不朽钝剑！')
                self.QB -= 1
                self.AB -= 1
                if self.judge(-1.5):
                    print('朽坏骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)
                    print('朽坏骷髅对你造成了物理伤害！')
            else:
                print('朽坏骷髅使用了不灭恶疾')
                self.AC -= 1
                self.QB -= 1
                self.AB -= 2
                if self.judge(-1.25):
                    print('朽坏骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 4)
                    print('朽坏骷髅对你造成了疾病伤害！')

# 炽焰骷髅 lv.5 远程


class Monster_BlzingSkeleton(Monster):
    def __init__(self):
        self.AC = 10
        self.HP = 18
        self.AB = 10
        self.QB = 3
        self.Name = '炽焰骷髅'
        self.Money = random.randint(20, 60)

    def do_fight_round(self, role):
        print('炽焰骷髅对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了炽焰骷髅的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('炽焰骷髅使用了烈焰球！')
                self.HP -= 1
                self.AB -= 1
                if self.judge(-2):
                    print('炽焰骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)
                    print('炽焰骷髅对你造成了火焰伤害！')
            elif how_to_fight <= 8:
                print('炽焰骷髅使用了炽焰爪！')
                self.HP -= 1
                self.AB -= 1
                if self.judge(-2):
                    print('炽焰骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)
                    print('炽焰骷髅对你造成了火焰伤害！')
            else:
                print('炽焰骷髅使用了炎空爆')
                self.AC -= 1
                self.QB -= 1
                self.HP -= 2
                if self.judge(-2):
                    print('炽焰骷髅的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 4)
                    print('炽焰骷髅对你造成了火焰伤害！')
# 幼年红龙 lv.6 强者


class Monster_YoungredDragon(Monster):
    def __init__(self):
        self.AC = 19
        self.HP = 26
        self.AB = 16
        self.QB = 12
        self.Name = '幼年红龙'
        self.Money = random.randint(40, 80)

    def do_fight_round(self, role):
        print('幼年红龙对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了幼年红龙的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('幼年红龙使用了啮咬攻击！')
                self.AB -= 2
                self.AC -= 1
                if self.judge(-2):
                    print('幼年红龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 5)
                    print('幼年红龙对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('幼年红龙使用了龙怒攻击！')
                self.HP -= 1
                self.AC -= 1
                if self.judge(-2):
                    print('幼年红龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(5, 7)+1
                    print('幼年红龙对你造成了物理伤害！')
            else:
                print('幼年红龙使用了龙息攻击')
                self.AC -= 3
                self.QB -= 1
                self.AB -= 2
                if self.judge(-2):
                    print('幼年红龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(7, 8)+1
                    print('幼年红龙对你造成了火焰伤害！')

# 龙裔法师 lv.4 头目 控制


class Monster_DragonWizard(Monster):
    def __init__(self):
        self.AC = 17
        self.HP = 18
        self.AB = 17
        self.QB = 18
        self.Name = '龙裔法师'
        self.Money = random.randint(40, 60)

    def do_fight_round(self, role):
        print('龙裔法师对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了龙裔法师的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('龙裔法师使用了法术攻击！')
                self.AB -= 2
                self.AC -= 1
                if self.judge(-2):
                    print('龙裔法师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)
                    role.AC -= random.randint(1, 2)
                    role.AB -= random.randint(0, 2)
                    role.QB -= random.randint(0, 2)
                    print('龙裔法师对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('龙裔法师使用了龙怒攻击！')
                self.HP -= 1
                self.AC -= 1
                if self.judge(-2):
                    print('龙裔法师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 4)
                    role.AC -= random.randint(0, 2)
                    role.AB -= random.randint(1, 2)
                    role.QB -= random.randint(0, 2)
                    print('龙裔法师对你造成了物理伤害！')
            else:
                print('龙裔法师使用了龙息攻击')
                self.AC -= 3
                self.QB -= 1
                self.AB -= 2
                if self.judge(-2):
                    print('龙裔法师的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)
                    role.AC -= random.randint(0, 2)
                    role.AB -= random.randint(0, 2)
                    role.QB -= random.randint(1, 2)
                    print('龙裔法师对你造成了元素伤害！')

# 木乃伊战士 lv.5  蛮战


class Monster_mummy(Monster):
    def __init__(self):
        self.AC = 16
        self.HP = 20
        self.AB = 15
        self.QB = 9
        self.Name = '木乃伊战士'
        self.Money = random.randint(48, 68)

    def do_fight_round(self, role):
        print('木乃伊战士对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了木乃伊战士的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('木乃伊战士使用了近战攻击！')
                self.AB -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('木乃伊战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)
                    role.AC -= random.randint(1, 2)
                    role.AB -= random.randint(0, 2)
                    print('木乃伊战士对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('木乃伊战士使用了木乃伊诅咒攻击！')
                self.HP -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('木乃伊战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)
                    role.AC -= random.randint(1, 2)
                    role.AB -= random.randint(1, 2)
                    role.QB = random.randint(1, 2)
                    print('木乃伊战士对你造成了诅咒伤害！')
            else:
                print('木乃伊战士使用了腐朽猛击')
                self.AC -= 4
                self.AB -= 4
                if self.judge(-2):
                    print('木乃伊战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(5, 6)+1
                    role.AC -= random.randint(1, 2)
                    role.AB -= random.randint(0, 2)
                    print('木乃伊战士对你造成了腐蚀伤害！')

# 吸血鬼 lv.5  伏兵


class Monster_vampire(Monster):
    def __init__(self):
        self.AC = 16
        self.HP = 17
        self.AB = 15
        self.QB = 17
        self.Name = '吸血鬼'
        self.Money = random.randint(45, 65)

    def do_fight_round(self, role):
        print('吸血鬼对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了吸血鬼的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('吸血鬼使用了近战攻击！')
                self.AB -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('吸血鬼的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)
                    self.HP += random.randint(0, 2)
                    print('吸血鬼对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('吸血鬼从天而降，对你进行了攻击！')
                self.HP -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('吸血鬼的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)
                    self.HP += random.randint(0, 2)
                    print('吸血鬼对你造成了物理伤害！')
            else:
                print('吸血鬼使用了吸血攻击')
                self.AC -= 4
                self.AB -= 4
                if self.judge(-2):
                    print('吸血鬼的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 5)+1
                    self.HP += random.randint(3, 4)
                    print('吸血鬼对你造成了吸血伤害！')

#  变异蝙蝠  lv.4 伏兵


class Monster_Bat(Monster):
    def __init__(self):
        self.AC = 14
        self.HP = 16
        self.AB = 13
        self.QB = 11
        self.Name = '变异蝙蝠'
        self.Money = random.randint(40, 60)

    def do_fight_round(self, role):
        print('变异蝙蝠对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了变异蝙蝠的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('变异蝙蝠使用了近战攻击！')
                self.AB -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('变异蝙蝠的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 3)

                    print('变异蝙蝠对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('变异蝙蝠从天而降，对你进行了攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('变异蝙蝠的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)

                    print('变异蝙蝠对你造成了物理伤害！')
            else:
                print('变异蝙蝠使用了尾削攻击')
                self.AC -= 2
                self.AB -= 2
                if self.judge(-2):
                    print('变异蝙蝠的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)

                    print('变异蝙蝠对你造成了物理伤害！')

#  变异熊  lv.5 蛮战


class Monster_Bear(Monster):
    def __init__(self):
        self.AC = 15
        self.HP = 19
        self.AB = 15
        self.QB = 9
        self.Name = '变异熊'
        self.Money = random.randint(48, 68)

    def do_fight_round(self, role):
        print('变异熊对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了变异熊的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('变异熊使用了近战攻击！')
                self.AB -= 2
                self.AC -= 2
                if self.judge(-2):
                    print('变异熊的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)

                    print('变异熊对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('变异熊使用了爪抓攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('变异熊的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 6)

                    print('变异熊对你造成了物理伤害！')
            else:
                print('变异熊使用了狂怒攻击')
                self.AC -= 3
                self.AB -= 3
                if self.judge(-2):
                    print('变异熊的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(5, 6)+1

                    print('变异熊对你造成了物理伤害！')

#  变异野猪  lv.4 蛮战


class Monster_Pig(Monster):
    def __init__(self):
        self.AC = 14
        self.HP = 17
        self.AB = 13
        self.QB = 9
        self.Name = '变异野猪'
        self.Money = random.randint(45, 55)

    def do_fight_round(self, role):
        print('变异野猪对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了变异野猪的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('变异野猪使用了抵撞攻击！')
                self.AB -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('变异野猪的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)+1

                    print('变异野猪对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('变异野猪使用了冲锋攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('变异野猪的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 5)

                    print('变异野猪对你造成了物理伤害！')
            else:
                print('变异野猪使用了暴烈冲锋攻击')
                self.AC -= 3
                self.AB -= 2
                if self.judge(-2):
                    print('变异野猪的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(5, 6)+1
                    role.AC -= random.randint(0, 1)+1
                    print('变异野猪对你造成了物理伤害！')

#  守卫巨像  lv.7 蛮战


class Monster_Colossus(Monster):
    def __init__(self):
        self.AC = 18
        self.HP = 25
        self.AB = 18
        self.QB = 5
        self.Name = '守卫巨像'
        self.Money = random.randint(70, 100)

    def do_fight_round(self, role):
        print('守卫巨像对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了守卫巨像的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('守卫巨像使用了挥砍攻击！')
                self.AB -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('守卫巨像的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 5)+1

                    print('守卫巨像对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('守卫巨像使用了力场武器攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('守卫巨像的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(6, 7)

                    print('守卫巨像对你造成了物理伤害！')
            else:
                print('守卫巨像使用了守卫之声攻击')
                self.AC -= 3
                self.AB -= 2
                if self.judge(-2):
                    print('守卫巨像的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(7, 9)+1
                    print('守卫巨像对你造成了物理伤害！')

#  矮人战士  lv.3 蛮战


class Monster_DwarfFighter(Monster):
    def __init__(self):
        self.AC = 14
        self.HP = 15
        self.AB = 13
        self.QB = 15
        self.Name = '矮人战士'
        self.Money = random.randint(35, 45)

    def do_fight_round(self, role):
        print('矮人战士对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了矮人战士的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('矮人战士使用了战锤攻击！')
                self.AB -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('矮人战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(2, 4)+1

                    print('矮人战士对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('矮人战士使用了弩攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('矮人战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)

                    print('矮人战士对你造成了物理伤害！')
            else:
                print('矮人战士使用了跳跃攻击')
                self.AC -= 1
                self.AB -= 2
                if self.judge(-2):
                    print('矮人战士的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 5)+1
                    print('矮人战士对你造成了物理伤害！')

#  人类佣兵  lv.3 蛮战


class Monster_Human(Monster):
    def __init__(self):
        self.AC = 15
        self.HP = 16
        self.AB = 14
        self.QB = 14
        self.Name = '人类佣兵'
        self.Money = random.randint(50, 60)

    def do_fight_round(self, role):
        print('人类佣兵对你发起了进攻！')

        if self.judge(role.QB - self.QB):
            print('你躲过了人类佣兵的攻击')
        else:
            how_to_fight = random.randint(1, 10)  # 三种攻击选中的概率比为4：4：2
            if how_to_fight <= 4:
                print('人类佣兵使用了短剑攻击！')
                self.AB -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('人类佣兵的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(1, 2)+1

                    print('人类佣兵对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('人类佣兵使用了弩攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('人类佣兵的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 4)

                    print('人类佣兵对你造成了物理伤害！')
            else:
                print('人类佣兵使用了手里剑攻击')
                self.AC -= 1
                self.AB -= 2
                if self.judge(-2):
                    print('人类佣兵的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)+1
                    print('人类佣兵对你造成了物理伤害！')


# 战士
class Role_Fighter(Role):
    def __init__(self):
        self.AC = 15
        self.HP = 10
        self.AB = 15
        self.QB = 8
        self.Name = '战士'
        Role.__init__(self)

    def do_fight_round(self, monster):
        print('你要做什么？', '你可以选择：', 'a: 战斗 / b: 逃避 / c: 躲避', sep='\n')

        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('请选择对应的动作 (a/b/c): ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            attack_way = input(
                '作为一名战士，你可以使用你的巨剑(AB-1，QB-1)，或用你有力的拳头（HP-1）向敌人挥去（a/b）：').lower()
            if attack_way == 'a':
                print('你选择了使用巨剑攻击\n加油！')
                self.AB -= 1
                self.QB += 1

                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= 8
            elif attack_way == 'b':
                print('你选择了使用拳头攻击, 加油!')
                self.HP -= 1
                if self.judge(monster.QB - self.QB - 1):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'攻击成功，{monster.Name}，血量降低！')
                    monster.HP -= 4

        elif action == 'b':
            print('WOW！你选择了', '逃避！（QB-1，HP+1）', 'Good Luck!', sep='\n')
            input('作为一名战士，你只能走着离开，按下任意一个键来继续下一步')
            self.QB -= 1
            self.HP += 1

            if self.judge(monster.QB - self.QB - 1):
                print('糟糕，逃避失败了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点HP')
            else:
                print('它没有看到你的离开！你安然无恙！')
                return True

        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1, QB+1)', 'Good Luck!', sep='\n')
            input('作为一名战士，你只能蹲下躲避，按下任意一个键来继续下一步')
            self.AC - 1
            self.QB += 1
            if self.judge(monster.QB - self.QB - 1):
                print('你没躲过它的攻击！你受伤了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点生命值')
            else:
                print('它没有发现你，你成功逃过一劫！')

# 法师


class Role_Wizard(Role):
    def __init__(self):
        self.AC = 10
        self.HP = 8
        self.AB = 15
        self.QB = 15
        self.Name = '法师'
        Role.__init__(self)

    def do_fight_round(self, monster):
        print('你要做什么？', '你可以选择：', 'a: 战斗 / b: 逃避 / c: 躲避', sep='\n')

        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('请选择对应的动作 (a/b/c): ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            attack_way = input('作为一名法师，你可以使用你的火球(AB-1，AC+1)，或用你的闪电（AB-1，AC+1），\n\
                或者使用冲击（AB-1，HP+1）敌人冲去（a/b/c）：').lower()
            if attack_way == 'a':
                print('你选择了使用火球攻击，加油！')
                self.AB -= 1
                self.AC += 1
                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'火球攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= random.randint(3, 6)

            elif attack_way == 'b':
                print('你选择了使用闪电攻击', '加油', sep='\n')
                self.AB -= 1
                self.AC += 1
                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= random.randint(2, 3)

            elif attack_way == 'c':
                print('你选择了使用冲击', '加油', sep='\n')
                self.AB -= 1
                self.HP += 1
                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= random.randint(2, 3)

        elif action == 'b':
            print('WOW！你选择了', '逃避！(QB-1，HP+1)', 'Good Luck!', sep='\n')
            input('作为一名法师，你只能瞬移，按下任意一个键来继续下一步')
            self.QB -= 1
            self.HP += 1
            if self.judge(monster.QB - self.QB - 1):
                print('糟糕，逃避失败了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点HP')
            else:
                print('它没有看到你的离开！你安然无恙！')
                return True

        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1,QB+1)', 'Good Luck!', sep='\n')
            input('作为一名法师，你只能使用隐身躲避，按下任意一个键来继续下一步')
            self.AC -= 1
            self.QB += 1
            if self.judge(monster.QB - self.QB - 1):
                print('你没躲过它的攻击！你受伤了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点生命值')
            else:
                print('它没有发现你，你成功逃过一劫！')


# 游侠
class Role_Ranger(Role):
    def __init__(self):
        self.AC = 8
        self.HP = 15
        self.AB = 10
        self.QB = 15
        self.Name = '游侠'
        Role.__init__(self)

    def do_fight_round(self, monster):
        print('你要做什么？', '你可以选择：', 'a: 战斗 / b: 逃避 / c: 躲避', sep='\n')
        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('请选择对应的动作 (a/b/c): ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            attack_way = input(
                '作为一名游侠，你可以使用你的弓箭(AB-1，AC+1)，或者使用你有力的拳头（HP-1）（a/b）').lower()
            if attack_way == 'a':
                print('你选择了使用弓箭攻击', '加油！', sep='\n')
                self.AB -= 1
                self.AC += 1
                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'弓箭攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= random.randint(3, 6)
            elif attack_way == 'b':
                print('你选择了使用拳头攻击', '加油', sep='\n')
                self.HP -= 1
                if self.judge(monster.QB - self.QB):
                    print(f'{monster.Name}躲过了你的的攻击')
                else:
                    print(f'拳头攻击成功，{monster.Name}遭到了重创！')
                    monster.HP -= random.randint(2, 3)

        elif action == 'b':
            print('WOW！你选择了', '逃避！(QB-1，AC+1)', 'Good Luck!', sep='\n')
            input('作为一名游侠，你只能跑，按下任意一个键来继续下一步')
            self.QB -= 1
            self.AC += 1
            if self.judge(monster.QB - self.QB - 1):
                print('糟糕，逃避失败了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点HP')
            else:
                print('它没有看到你的离开！你安然无恙！')
                return True
        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1,AB+1)', 'Good Luck!', sep='\n')
            input('作为一名游侠，你只能趴下躲避，按下任意一个键来继续下一步')
            self.AC -= 1
            self.AB += 1
            if self.judge(monster.QB - self.QB - 1):
                print('你没躲过它的攻击！你受伤了！')
                self.HP -= random.randint(2, 4)
                print(f'你还剩下{self.HP}点生命值')
            else:
                print('它没有发现你，你成功逃过一劫！')


def display_cookie_for_input():
    openlog = input()
    if openlog == '/log.makers':
        print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
              'PRODUCTION DIRECTOR(制作总监):Eason Chen', 'OPTIMIZATION（代码总监）:Jason Chen',
              'ORIGINALITY FROM(创意来源):Chloe Zhao&Wind Is blowing Li&Amy Wu', sep='\n')
        time.sleep(1)
        print('Thanks For Playing our Game! :D')
        time.sleep(2)
        sys.exit(0)
    else:
        print('Thanks For Playing our Game! :D')
        time.sleep(2)
        sys.exit(0)


def Egg():
    print('黑暗.')
    time.sleep(0.5)
    print('黑暗..')
    time.sleep(0.5)
    print('黑暗...')
    print('一丝光…')
    time.sleep(0.5)
    print('系统：你好，你叫什么名字？')
    Name = input()
    print('系统：哦，你好，', Name)
    time.sleep(0.5)
    print(Name, ':你……你是谁？！我怎么会在这里！话……话说我叫啥来着？')
    time.sleep(0.5)
    print('系统：你这么快就忘了？不过没关系，反正你终究不会知道……言归正传，', Name, '听着，找到他')
    time.sleep(0.5)
    print(Name, ':他？')
    time.sleep(0.5)
    print('系统：你会知道的，我会跟随你的', Name, '.不过，在此之前……')
    time.sleep(0.5)
    print('系统：/world.003.', Name, '.set(0)')
    time.sleep(1)
    print(Name, ':HELLO,WORLD!')
    time.sleep(2)


def display_copyright():
    print('~~~~欢迎到来~~~~', 'DRAGON ISLAND: FIRST START',
          '这部中文游戏由HACKER.C.D.GAME STUDIO开发制作.祝您游玩愉快.', '按下回车键以开始游戏', '—'*60, sep='\n')

    openEgg = input()
    if openEgg == '/Egg.open':
        Egg()
    else:
        print('游戏开始', '-'*60, sep='\n')

# 显示游戏说明（1）


def display_game_introduce():
    print('欢迎来到龙之岛.', '你眼前有两个山洞,', '里面分别有两条龙:一条温顺友好;一条凶恶残忍.',
          '选择权在你手中，自己作出选择吧！', sep='\n')


def go_store(player):
    print('现在是购买环节，你可以购买：', '生命药水——帮你恢复3点的HP',
          '强化药水——帮你恢复1点的AC与2点的AB', '恢复药水——帮你恢复1点HP与2点的QB', sep='\n')
    print(
        f'以下为你的各项点数：AC: {player.AC}, HP: {player.HP}, QB: {player.QB}, Money: {player.Money}')
    buywhat = input('你要买什么呢？以上的药水价格分别为150M/200M/200M(a/b/c/)')
    if buywhat == 'a':
        if player.Money >= 150:
            print('你确认要花费150¥购买生命药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 150
                print('你购买了生命药水，你可以在打开背包时,输入“生命药水”来使用它')
                player.Bag.append('生命药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')

        else:
            print('Money不足')
    elif buywhat == 'b':
        if player.Money >= 200:
            print('你确认要花费200¥购买强化药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 200
                print('你购买了强化药水，你可以在打开背包时,输入“强化药水”来使用它')
                player.Bag.append('强化药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')

        else:
            print('Money不足')
    elif buywhat == 'c':
        if player.Money >= 200:
            print('你确认要花费200¥购买恢复药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 200
                print('你购买了恢复药水，你可以在打开背包时,输入“恢复药水”来使用它')
                player.Bag.append('恢复药水')
            elif passby == 'b':
                print('你不想购买它')

        else:
            print('Money不足')

    OPENBAG = input('是否要打开背包?(a/b)')
    if OPENBAG == 'a':
        use = input(f'你包里有{player.Bag} 你要使用什么？(每次只能用一种药水)')
        if use == '生命药水':
            if '生命药水' in player.Bag:
                passuse = input('你要使用生命药水吗？(a/b)')
                if passuse == 'a':
                    player.HP += 3
                    player.Bag.remove('生命药水')
                    print('你使用了生命药水，恢复了3点HP')
                elif passuse == 'b':
                    print('你合上了背包')
                else:
                    print('404 NOT FOUND :(')
        elif use == '强化药水':
            if '强化药水' in player.Bag:
                passuse = input('你要使用强化药水吗？(a/b)')
                if passuse == 'a':
                    player.AC += 1
                    player.AB += 2
                    player.Bag.remove('强化药水')
                    print('你使用了强化药水，恢复了1点AC与2点AB')
                elif passuse == 'b':
                    print('你合上了背包')
            else:
                print('404 NOT FOUND :(')
        elif use == '恢复药水':
            if '恢复药水' in player.Bag:
                print('你要使用恢复药水吗？(a/b)')
                passuse = input()
                if passuse == 'a':
                    player.HP += 1
                    player.QB += 2
                    player.Bag.remove('恢复药水')
                    print('你使用了恢复药水，恢复了1点HP与2点QB')
                elif passuse == 'b':
                    print('你合上了背包')
                else:
                    print('404 NOT FOUND :(')
        else:
            print('404 NOT FOUND :(')
    else:
        print('你离开了此地')


def create_role():
    print('恭喜你闯过了第一关！', '不过你的路还很长，', '接下来你需要探索这座岛，', '这座离奇，又充满着神秘气息的岛屿……',
          '找到宝库，也许看守着宝库的智者会告诉你如何离开！', sep='\n')  # 简介

    time.sleep(2)

    # 选择职业
    option = input(
        '首先，你得作出一个选择\n你要为自己选择一个职业\n一个没有职业的人，好比没有目标的炸弹\n你面前有三种选择\n战士、法师与游侠\n作出你的选择吧！（a/b/c）').lower()
    while option not in ['a', 'b', 'c']:
        option = input('请选择对应的职业 (a/b/c)').lower()

    if option == 'a':
        player = Role_Fighter()
    elif option == 'b':
        player = Role_Wizard()
    elif option == 'c':
        player = Role_Ranger()

    player.display_role_introduce()

    return player


def create_monster():
    monster_cls_list = [
        Monster_YoungWhiteDragon,
        Monster_BlzingSkeleton,
        Monster_DecrepitSkeleton,
        Monster_GoblinCutter,
        Monster_GoblinHexer,
        Monster_YoungBlackDragon
    ]
    monster_cls = random.choice(monster_cls_list)

    return monster_cls()


def create_land(total_rounds):
    land = ''
    if total_rounds < 5:
        land = random.choice(land_list[1:])
    else:
        land = random.choice(land_list)

    return land

# 第一幕，选择洞穴


def stage1_cave():
    # 让用户选择一个洞穴
    cave = ''
    while cave != '1' and cave != '2':  # 如果用户写出了正确的洞穴，则跳出这个循环
        cave = input('选择一个洞穴吧！(1或2)')

    print('你进入了山洞...')
    time.sleep(2)

    seed = random.randint(1, 5)

    if seed <= 4:
        print('干的好...')
        time.sleep(1)
        print('你进入了温顺龙的洞穴！它给了你...')
        time.sleep(2)
        print('宝库的钥匙！\n')
        return True
    else:
        print('干的好...')
        time.sleep(1)
        print('你被凶恶龙一口吃了！oops!\n')
        return False


if __name__ == '__main__':
    display_copyright()

    while True:  # 用户没选择退出就一直执行游戏循环
        display_game_introduce()

        if stage1_cave():
            role = create_role()
            total_rounds = 0
            while True:
                land = create_land(total_rounds)
                total_rounds += 1
                monster = create_monster()
                if land == '宝库':
                    # 如果选中宝库，那么，结束游戏
                    print('Good job! 你找到了宝库！智者告诉了你... (见下一部:Dranon Island II)')
                    display_cookie_for_input()
                    break
                else:
                    print('你进入了' + land + ',遇到了' + monster.Name)
                    print(f' {monster.Name}的各项参数是:', monster.get_status_str())

                escaped = False
                while True:
                    if monster.QB > role.QB:
                        monster.do_fight_round(role)
                        if (not monster.is_alive()) or (not role.is_alive()):
                            break

                        escaped = role.do_fight_round(monster)
                        if escaped or (not monster.is_alive()) or (not role.is_alive()):
                            break
                    else:  # role.QB >= monster.QB
                        escaped = role.do_fight_round(monster)
                        if escaped or (not monster.is_alive()) or (not role.is_alive()):
                            break

                        monster.do_fight_round(role)
                        if (not monster.is_alive()) or (not role.is_alive()):
                            break

                    print('你的各项参数是:', role.get_status_str())
                    print(f'{monster.Name}的各项参数是:', monster.get_status_str())
                    time.sleep(2)

                if escaped:
                    continue
                elif role.is_alive():
                    print(f'你击杀了{monster.Name}， 获得了奖励：Money {monster.Money}M')
                    role.Money += monster.Money
                    print('你的各项参数是:', role.get_status_str())
                else:
                    print('OOPS! 你死了！ 你死亡时的各项参数是: ', role.get_status_str())
                    display_cookie_for_input()
                    break

                passin = input('你是否要进入商店？是(a)/否(b)')
                if passin == 'a':
                    go_store(role)

        playAgain = input('想再来一局不？(y/n)').lower()  # 检测键入
        if playAgain != 'yes' and playAgain != 'y':
            break
