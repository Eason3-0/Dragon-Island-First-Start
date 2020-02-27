# -*- coding:utf-8 -*-

from abc import ABC, abstractmethod
import random
import time
import math


# 怪兽和角色的基础类
class Creature(ABC):
    @abstractmethod
    def get_status_str(self):  # 状态字符串
        pass

    # @abstractmethod
    def fight_round(self, opponent):
        pass

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
        self.introduce = [f'你选择了{self.Name}！这是一个不错的职业，只是…\n你首先要了解：我们的世界由五大属性组成：',
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


# 幼年白龙 lv.3 强者 蛮战
class Monster_YoungWhiteDragon(Monster):
    def __init__(self):
        self.AC = 16
        self.HP = 15
        self.AB = 12
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
                else:
                    role.HP -= random.randint(2, 4)
                    print('幼年白龙对你造成了物理伤害！')
            elif how_to_fight <= 8:
                print('幼年白龙使用了龙怒攻击！')
                self.HP -= 1
                self.AC -= 2
                if self.judge(-2):
                    print('幼年白龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(3, 5)
                    print('幼年白龙对你造成了物理伤害！')
            else:
                print('幼年白龙使用了龙息攻击')
                self.AC -= 4
                self.QB -= 2
                self.AB -= 2
                if self.judge(-2):
                    print('幼年白龙的攻击失败了！你没有受到伤害')
                else:
                    role.HP -= random.randint(4, 7)
                    print('幼年白龙对你造成了寒冰伤害！')


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
            how_to_fight = random.randint(1, 10)# 三种攻击选中的概率比为4：4：2
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
            how_to_fight = random.randint(1, 10)# 三种攻击选中的概率比为4：4：2
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
            how_to_fight = random.randint(1, 10)# 三种攻击选中的概率比为4：4：2
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
        self.Money = random.randint(35, 70)

    def do_fight_round(self, role):
        print('炽焰骷髅对你发起了进攻！')
        
        if self.judge(role.QB - self.QB):
            print('你躲过了炽焰骷髅的攻击')
        else:
            how_to_fight = random.randint(1, 10)# 三种攻击选中的概率比为4：4：2
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
            attack_way = input('作为一名战士，你可以使用你的巨剑(AB-1，QB-1)，或用你有力的拳头（HP-1）向敌人挥去（a/b）：').lower()
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
        action=''
        while action not in ['a', 'b', 'c']:
            action=input('请选择对应的动作 (a/b/c): ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            attack_way=input('作为一名游侠，你可以使用你的弓箭(AB-1，AC+1)，或者使用你有力的拳头（HP-1）（a/b）').lower()
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
