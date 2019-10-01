import random
import time
import sys
import abc

land_list = ['宝库', '草地', '高山', '池塘', '火山', '黑森林', '森林',
                 '废墟', '神殿', '沙漠', '沼泽', '矿洞', '大海']  # 创立一个地点列表备用
npc_list = ['一条幼年白龙', '一个哥布林', '一个巨人', '一个机器人', '一个骷髅','一个僵尸','一朵曼陀罗花']  # 创建一个人物列表备用
attack_results = ['它攻击了你！你受伤了！', '你杀死了它！你赢了！',
                    '你杀死了它！你赢了！', '你杀死了它！你赢了！', '你杀死了它！你赢了！']
escape_results = ['它没有看到你的离开！你安然无恙！', '它攻击了你！你受伤了！',
                    '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', ]
hide_results = ['你没躲过它的攻击！你受伤了！', '它没有发现你，你成功逃过一劫！',
                '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！']

def display_cookie_for_input():
    openlog = input()
    if openlog == '/log.makers':
        print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
            'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason',sep='\n')
        time.sleep(2)
        print('Thanks For Playing My Game! :D')
        time.sleep(2)
        sys.exit(0)
    else:
        print('Thanks For Playing My Game! :D')
        time.sleep(2)
        sys.exit(0)

def Egg():
    print('黑暗.')
    time.sleep(1)
    print('黑暗..')
    time.sleep(1)
    print('黑暗...')
    print('一丝光…')
    time.sleep(1)
    print('系统：你好，你叫什么名字？')
    Name = input()
    print('系统：哦，你好，',Name)
    time.sleep(1)
    print(Name,':你……你是谁？！我怎么会在这里！话……话说我叫啥来着？')
    time.sleep(1)
    print('系统：你这么快就忘了？不过没关系，反正你终究不会知道……言归正传，',Name,'听着，找到他')
    time.sleep(1)
    print(Name,':他？')
    time.sleep(1)
    print('系统：你会知道的，我会跟随你的',Name,'.不过，在此之前……')
    time.sleep(1)
    print('系统：/world.003.',Name,'.set(0)')
    time.sleep(1)
    print(Name,':HELLO,WORLD!')
    time.sleep(2)

# 网游职业的基础类
class Role(metaclass=abc.ABCMeta):
    AC = 0
    AB = 0
    HP = 0
    QB = 0
    Money = 100
    Bag = [] # 背包

    total_rounds = 0

    def get_status_str(self):
        return f'AC: {self.AC}, AB: {self.AB}, HP: {self.HP}, QB: {self.QB}, Money: {self.Money}'

    def check_status(self):
        if self.AC == 0 or self.AB == 0 or self.HP == 0 or self.QB == 0:
            print('OOPS! 你死了！ 你死亡时的各项参数是: ', self.get_status_str())
            display_cookie_for_input()
            return False
        else:
            print('你的各项参数是:', self.get_status_str())
            return True

    def display_role_intro(self):
        pass

# 战士
class Role_Fighter(Role):
    def __init__(self):
        self.AC = 15
        self.HP = 10
        self.AB = 15
        self.QB = 8
        self.Name = '战士'
    
    def display_role_intro(self):
        print(f'你选择了{self.Name}！', '这是一个不错的职业，只是…', '你首先要了解：', '我们的世界由五大属性组成：', sep='\n')
        time.sleep(2)
        print('分别是：', '防御值（AC）：在你遭受攻击时挡住攻击', sep='\n')
        time.sleep(2)
        print('生命值（HP）：在你受到攻击时遭受的伤害')
        time.sleep(2)
        print('攻击加值（AB）：在你挥出巨剑时带给敌方的痛苦感受')
        time.sleep(2)
        print('灵敏值（QB）：在你躲过敌方致命一击时的冲刺')
        time.sleep(2)
        print('与金钱（Money）：你胜利击退可恶的铁脑壳时获取的奖赏')
        time.sleep(2)
        print(f'当你了解了这些之后，你需要知道{self.Name}的各项属性', 'AC = 15', 'HP = 10', 'AB = 15',
              'QB = 8', 'Money = 100', '(任何一项为0，你都会死亡(除Money之外))', sep='\n')
    
    def do_fight_round(self):
        land = ''
        if self.total_rounds < 5:
            land = random.choice(land_list[1:])
        else:
            land = random.choice(land_list)

        if land == '宝库':
            # 如果选中宝库，那么，结束游戏
            print('Good job! 你找到了宝库！智者告诉了你... (见下一部:Dranon Island II)')
            display_cookie_for_input()
            return False
            
        # 设立一个语境，将随机选中的词语填充入内
        print('你进入了' + land + ',遇到了' + random.choice(npc_list))
        print('你要做什么？', '你可以选择：', '战斗', '逃避', '躲避', sep='\n')
        
        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('输入“a/b/c”来选择对应的动作: ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            print('作为一名战士，你可以使用你的巨剑(AB-1，QB-1)，或用你有力的拳头（HP-1）向敌人挥去（a/b）')
            attack_way = input().lower()
            if attack_way == 'a':
                print('你选择了使用巨剑攻击', '加油！', sep='\n')
                self.AB -= 1
                self.QB += 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 3)

                    print(f'你还剩下{self.HP}点HP')
                    #store()

                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 50)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

            elif attack_way == 'b':
                print('你选择了使用拳头攻击', '加油', sep='\n')
                self.HP -= 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 3)
                    print(f'你还剩下{self.HP}点HP')
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 50)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

        elif action == 'b':
            print('WOW！你选择了', '逃避！（QB-1，HP+1）', 'Good Luck!', sep='\n')
            print('作为一名战士，你只能走着离开，按下任意一个键来继续下一步')
            input()
            self.QB -= 1
            self.HP += 1
            escape_instance = random.choice(escape_results)
            if escape_instance == '它攻击了你！你受伤了！':
                print(escape_instance)
                self.HP -= random.randint(2, 4)
                print('你还剩下', self.HP, '点HP')
            elif escape_instance == '它没有看到你的离开！你安然无恙！':
                self.Money += random.randint(1, 50)
                print(escape_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
               
        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1,QB+1)', 'Good Luck!', sep='\n')
            print('作为一名战士，你只能蹲下躲避，按下任意一个键来继续下一步')
            input()
            self.AC - 1
            self.QB += 1
            hide_instance = random.choice(hide_results)
            if hide_instance == '你没躲过它的攻击！你受伤了！':
                print(hide_instance)
                self.HP -= random.randint(2, 4)
                print('你还剩下', self.HP, '点HP')
            elif hide_instance == '它没有发现你，你成功逃过一劫！':
                self.Money += random.randint(1, 50)
                print(hide_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
        
        self.total_rounds += 1

# 法师
class Role_Wizard(Role):
    def __init__(self):
        self.AC = 10
        self.HP = 8
        self.AB = 15
        self.QB = 15
        self.Name = '法师'

    def display_role_intro(self):
        print(f'你选择了{self.Name}！', '这是一个不错的职业，只是…', '你首先要了解：', '我们的世界由五大属性组成：', sep='\n')
        time.sleep(2)
        print('分别是：', '防御值（AC）：在你遭受攻击时挡住攻击', sep='\n')
        time.sleep(2)
        print('生命值（HP）：在你受到攻击时遭受的伤害')
        time.sleep(2)
        print('攻击加值（AB）：在你挥出巨剑时带给敌方的痛苦感受')
        time.sleep(2)
        print('灵敏值（QB）：在你躲过敌方致命一击时的冲刺')
        time.sleep(2)
        print('与金钱（Money）：你胜利击退可恶的铁脑壳时获取的奖赏')
        time.sleep(2)
        print(f'当你了解了这些之后，你需要知道{self.Name}的各项属性', 'AC = 10', 'HP = 8', 'AB = 15',
              'QB = 15', 'Money = 100', '(任何一项为0，你都会死亡(除Money之外))', sep='\n')

    def do_fight_round(self):
        land = ''
        if self.total_rounds < 5:
            land = random.choice(land_list[1:])
        else:
            land = random.choice(land_list)

        if land == '宝库':
            # 如果选中宝库，那么，结束游戏
            print('Good job! 你找到了宝库！智者告诉了你... (见下一部:Dranon Island II)')
            display_cookie_for_input()
            return False
            
        # 设立一个语境，将随机选中的词语填充入内
        print('你进入了' + land + ',遇到了' + random.choice(npc_list))
        print('你要做什么？', '你可以选择：', '战斗', '逃避', '躲避', sep='\n')
        
        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('输入“a/b/c”来选择对应的动作: ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            print('作为一名法师，你可以使用你的火球(AB-1，AC+1)，或用你的闪电（AB-1，AC+1），或者使用冲击（AB-1，HP+1）敌人冲去（a/b/c）')
            attack_way = input().lower()
            if attack_way == 'a':
                print('你选择了使用火球攻击', '加油！', sep='\n')
                self.AB -= 1
                self.AC += 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 2)
                    print(f'你还剩下{self.HP}点HP')
                    #store()
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 45)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

            elif attack_way == 'b':
                print('你选择了使用闪电攻击', '加油', sep='\n')
                self.AB -= 1
                self.AC += 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 2)
                    print(f'你还剩下{self.HP}点HP')
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 45)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

            elif attack_way == 'c':
                print('你选择了使用冲击', '加油', sep='\n')
                self.AB -= 1
                self.HP += 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 2)
                    print(f'你还剩下{self.HP}点HP')
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 45)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')


        elif action == 'b':
            print('WOW！你选择了', '逃避！(QB-1，HP+1)', 'Good Luck!', sep='\n')
            print('作为一名法师，你只能瞬移，按下任意一个键来继续下一步')
            input()
            self.QB -= 1
            self.HP += 1
            escape_instance = random.choice(escape_results)
            if escape_instance == '它攻击了你！你受伤了！':
                print(escape_instance)
                self.HP -= random.randint(2, 3)
                print('你还剩下', self.HP, '点HP')
            elif escape_instance == '它没有看到你的离开！你安然无恙！':
                self.Money += random.randint(1, 35)
                print(escape_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
               
        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1,QB+1)', 'Good Luck!', sep='\n')
            print('作为一名法师，你只能使用隐身躲避，按下任意一个键来继续下一步')
            input()
            self.AC -= 1
            self.QB += 1
            hide_instance = random.choice(hide_results)
            if hide_instance == '你没躲过它的攻击！你受伤了！':
                print(hide_instance)
                self.HP -= random.randint(2, 3)
                print('你还剩下', self.HP, '点HP')
            elif hide_instance == '它没有发现你，你成功逃过一劫！':
                self.Money += random.randint(1, 40)
                print(hide_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
        
        self.total_rounds += 1
    
# 游侠
class Role_Ranger(Role):
    def __init__(self):
        self.AC = 8
        self.HP = 15
        self.AB = 10
        self.QB = 15
        self.Name = '游侠'
    
    def display_role_intro(self):
        print(f'你选择了{self.Name}！', '这是一个不错的职业，只是…', '你首先要了解：', '我们的世界由五大属性组成：', sep='\n')
        time.sleep(2)
        print('分别是：', '防御值（AC）：在你遭受攻击时挡住攻击', sep='\n')
        time.sleep(2)
        print('生命值（HP）：在你受到攻击时遭受的伤害')
        time.sleep(2)
        print('攻击加值（AB）：在你挥出巨剑时带给敌方的痛苦感受')
        time.sleep(2)
        print('灵敏值（QB）：在你躲过敌方致命一击时的冲刺')
        time.sleep(2)
        print('与金钱（Money）：你胜利击退可恶的铁脑壳时获取的奖赏')
        time.sleep(2)
        print(f'当你了解了这些之后，你需要知道{self.Name}的各项属性', 'AC = 8', 'HP = 15', 'AB = 10',
              'QB = 15', 'Money = 100', '(任何一项为0，你都会死亡(除Money之外))', sep='\n')

    def do_fight_round(self):
        land = ''
        if self.total_rounds < 5:
            land = random.choice(land_list[1:])
        else:
            land = random.choice(land_list)

        if land == '宝库':
            # 如果选中宝库，那么，结束游戏
            print('Good job! 你找到了宝库！智者告诉了你... (见下一部:Dranon Island II)')
            display_cookie_for_input()
            return False
            
        # 设立一个语境，将随机选中的词语填充入内
        print('你进入了' + land + ',遇到了' + random.choice(npc_list))
        print('你要做什么？', '你可以选择：', '战斗', '逃避', '躲避', sep='\n')
        
        action = ''
        while action not in ['a', 'b', 'c']:
            action = input('输入“a/b/c”来选择对应的动作: ').lower()

        if action == 'a':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            print('作为一名游侠，你可以使用你的弓箭(AB-1，AC+1)，或者使用你有力的拳头（HP-1）（a/b）')
            attack_way = input().lower()
            if attack_way == 'a':
                print('你选择了使用弓箭攻击', '加油！', sep='\n')
                self.AB -= 1
                self.AC += 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 4)
                    print(f'你还剩下{self.HP}点HP')
                    #store()
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 55)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

            elif attack_way == 'b':
                print('你选择了使用拳头攻击', '加油', sep='\n')
                self.HP -= 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    self.HP -= random.randint(1, 4)
                    print(f'你还剩下{self.HP}点HP')
                elif attack_instance == '你杀死了它！你赢了！':
                    self.Money += random.randint(1, 50)
                    print(attack_instance, '你的战利品是金币，你现在有', self.Money, '个金币')

        elif action == 'b':
            print('WOW！你选择了', '逃避！(QB-1，AC+1)', 'Good Luck!', sep='\n')
            print('作为一名游侠，你只能跑，按下任意一个键来继续下一步')
            input()
            self.QB -= 1
            self.AC += 1
            escape_instance = random.choice(escape_results)
            if escape_instance == '它攻击了你！你受伤了！':
                print(escape_instance)
                self.HP -= random.randint(2, 5)
                print('你还剩下', self.HP, '点HP')
            elif escape_instance == '它没有看到你的离开！你安然无恙！':
                self.Money += random.randint(1, 55)
                print(escape_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
               
        elif action == 'c':
            print('WOW！你选择了', '躲避！(AC-1,AB+1)', 'Good Luck!', sep='\n')
            print('作为一名游侠，你只能趴下躲避，按下任意一个键来继续下一步')
            input()
            self.AC -= 1
            self.AB += 1
            hide_instance = random.choice(hide_results)
            if hide_instance == '你没躲过它的攻击！你受伤了！':
                print(hide_instance)
                self.HP -= random.randint(2, 5)
                print('你还剩下', self.HP, '点HP')
            elif hide_instance == '它没有发现你，你成功逃过一劫！':
                self.Money += random.randint(1, 50)
                print(hide_instance, '你的战利品是金币，你现在有', self.Money, '个金币')
        
        self.total_rounds += 1
      

def display_copyright():
    print('~~~~欢迎到来~~~~', 'DRAGON ISLAND: FIRST START', 
    '这部中文游戏由HACKER.C.D.GAME STUDIO开发制作.游玩愉快.','按下回车键以开始游戏','—'*60, sep='\n')
    openEgg = input()
    if openEgg == '/Egg.open':
        Egg()
    else:
        print('游戏开始','-'*60,sep='\n')

# 显示游戏说明（1）
def display_intro():
    print('欢迎来到龙之岛.', '你眼前有两个山洞,', '里面分别有两条龙:一条温顺友好;一条凶恶残忍.',
          '选择权在你手中，自己作出选择吧！', sep='\n')

def go_store(player):
    print('现在是购买环节，你可以购买：', '生命药水——帮你恢复3点的HP',
          '强化药水——帮你恢复1点的AC与2点的AB', '恢复药水——帮你恢复1点HP与2点的QB', sep='\n')
    print(f'以下为你的各项点数：AC: {player.AC}, HP: {player.HP}, QB: {player.QB}, Money{player.Money}')
    bywhat = input('你要买什么呢？以上的药水价格分别为150¥/200¥/200¥/使用背包中的药水（a/b/c/代码）')
    if bywhat == '/open.Bag':
        use = input(f'你包里有{player.Bag} 你要使用什么？')
        if use == '/use.HP':
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
        elif use == '/use.UP':
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
        elif use == '/use.BR':
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
    elif bywhat == 'a':
        if player.Money > 150:
            print('你确认要花费150¥购买生命药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 150
                print('你购买了生命药水，你可以在之后的这个时候输入：/open.Bag，接下来输入；/use.HP来使用它')
                player.Bag.append('生命药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    elif bywhat == 'b':
        if player.Money > 200:
            print('你确认要花费200¥购买强化药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 200
                print('你购买了强化药水，你可以在之后的这个时候输入：/open.Bag，接下来输入；/use.UP来使用它')
                player.Bag.append('强化药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    elif bywhat == 'c':
        if player.Money > 200:
            print('你确认要花费200¥购买恢复药水吗？a/b')
            passby = input()
            if passby == 'a':
                player.Money -= 200
                print('你购买了恢复药水，你可以在之后的这个时候输入：/open.Bag，接下来输入；/use.BR来使用它')
                player.Bag.append('恢复药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    else:
        print('你离开了此地')


def create_charactor():
    print('恭喜你闯过了第一关！', '不过你的路还很长，', '接下来你需要探索这座岛，',
          '找到宝库，也许智者会告诉你如何离开！', sep='\n')  # 简介
    
    time.sleep(2)
    # 选择职业
    print('首先，你得作出一个选择', '你要为自己选择一个职业', '一个没有职业的人，好比没有目标的炸弹',
          '你面前有三种选择', '战士、法师与游侠', '作出你的选择吧！（a/b/c）', sep='\n')
    
    option = input().lower()
    while option not in ['a', 'b', 'c']:
        print('输入“a/b/c”来选择对应的职业')
        option = input().lower()

    if option == 'a':
        player = Role_Fighter()
        player.display_role_intro()
    elif option == 'b':
        player = Role_Wizard()
        player.display_role_intro()
    elif option == 'c':
        player = Role_Ranger()
        player.display_role_intro()
    
    return player

# 第一幕，选择洞穴
def stage1_cave():
    # 让用户选择一个洞穴
    cave = ''
    while cave != '1' and cave != '2':  # 如果用户写出了正确的洞穴，则跳出这个循环
        print('选择一个洞穴吧！(1或2)')
        cave = input()
    
    print('你进入了山洞...')
    time.sleep(2)

    seed = random.randint(1, 5)

    if seed <= 4:
        print('干的好...')
        time.sleep(2)
        print('你进入了温顺龙的洞穴！它给了你...')
        time.sleep(2)
        print('宝库的钥匙！\n')
        return True
    else:
        print('干的好...')
        time.sleep(2)
        print('你被凶恶龙一口吃了！oops!\n')
        return False

if __name__ == '__main__':
    display_copyright()

    while True:  # 设立一个检测用户键入的程序
        display_intro()

        if stage1_cave():
            player = create_charactor()
            while True:
                player.do_fight_round()

                if not player.check_status():
                    break

                print('你是否要进入商店？a/b')
                passin = input()
                if passin == 'a':
                    go_store(player)

        playAgain = input('想再来一局不？(y/n)').lower()  # 检测键入
        if playAgain != 'yes' and playAgain != 'y':
            break