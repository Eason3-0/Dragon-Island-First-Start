import random
import time
import sys

AC = 0
HP = 0
QB = 0
Money = 100
bag = []
AB = 0

def check():
    if AC == 0:
        print('OOPS!你死了！你的死亡时各项参数是:', 'AC:', AC,
              'HP:', HP, 'QB:', QB, 'Money:', Money)
        openlog = input()
        if openlog == '/log.makers':
            print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
                  'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason')
            time.sleep(2)
            print('Thanks For Playing! :D')
            time.sleep(2)
            sys.exit(0)
        else:
            sys.exit(0)
    elif AB == 0:
        print('OOPS!你死了！你的死亡时各项参数是:', 'AC:', AC,
              'HP:', HP, 'QB:', QB, 'Money:', Money)
        openlog = input()
        if openlog == '/log.makers':
            print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
                  'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason')
            time.sleep(2)
            print('Thanks For Playing! :D')
            time.sleep(2)
            sys.exit(0)
        else:
            sys.exit(0)
    elif HP == 0:
        print('OOPS!你死了！你的死亡时各项参数是:', 'AC:', AC,
              'HP:', HP, 'QB:', QB, 'Money:', Money)
        openlog = input()
        if openlog == '/log.makers':
            print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
                  'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason')
            time.sleep(2)
            print('Thanks For Playing! :D')
            time.sleep(2)
            sys.exit(0)
        else:
            sys.exit(0)
    elif QB == 0:
        print('OOPS!你死了！你的死亡时各项参数是:', 'AC:', AC,
              'HP:', HP, 'QB:', QB, 'Money:', Money)
        openlog = input()
        if openlog == '/log.makers':
            print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
                  'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason')
            time.sleep(2)
            print('Thanks For Playing! :D')
            time.sleep(2)
            sys.exit(0)
        else:
            sys.exit(0)
    else:
        print('HP:',HP,'AC:',AC,'AB:',AB,'QB:',QB,'Money',Money)

def store():
    global AC, HP, QB, Money
    print('现在是购买环节，你可以购买：', '生命药水——帮你恢复3点的HP',
          '强化药水——帮你恢复1点的AC与2点的AB', '恢复药水——帮你恢复1点HP与2点的QB', sep='\n')
    print('以下为你的各项点数：', AC, HP, QB, Money, sep='\n')
    print('你要买什么呢？以上的药水价格分别为150¥/200¥/200¥/使用背包中的药水（a/b/c/代码）')
    bywhat = input()
    if bywhat == '/open.bag':
        print('你包里有', bag, '你要使用什么？')
        use = input()
        if use == '/use.HP':
            if '生命药水' in bag:
                print('你要使用生命药水吗？(a/b)')
                passuse = input()
                if passuse == 'a':
                    HP = HP + 3
                    bag.remove('生命药水')
                    print('你使用了生命药水，恢复了3点HP')
                elif passuse == 'b':
                    print('你合上了背包')
            else:
                print('404 NOT FOUND :(')
        elif use == '/use.UP':
            if '强化药水' in bag:
                print('你要使用强化药水吗？(a/b)')
                passuse = input()
                if passuse == 'a':
                    AC = AC + 1
                    AB = AB + 2
                    bag.remove('强化药水')
                    print('你使用了强化药水，恢复了1点AC与2点AB')
                elif passuse == 'b':
                    print('你合上了背包')
            else:
                print('404 NOT FOUND :(')
        elif use == '/use.BR':
            if '恢复药水' in bag:
                print('你要使用恢复药水吗？(a/b)')
                passuse = input()
                if passuse == 'a':
                    HP = HP + 1
                    QB = QB + 2
                    bag.remove('恢复药水')
                    print('你使用了恢复药水，恢复了1点HP与2点QB')
                elif passuse == 'b':
                    print('你合上了背包')
                else:
                    print('404 NOT FOUND :(')
            else:
                print('404 NOT FOUND :(')
    elif bywhat == 'a':
        if Money > 150:
            print('你确认要花费150¥购买生命药水吗？a/b')
            passby = input()
            if passby == 'a':
                Money = Money - 150
                print('你购买了生命药水，你可以在之后的这个时候输入：/open.bag，接下来输入；/use.HP来使用它')
                bag.append('生命药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    elif bywhat == 'b':
        if Money > 200:
            print('你确认要花费200¥购买强化药水吗？a/b')
            passby = input()
            if passby == 'a':
                Money = Money - 200
                print('你购买了强化药水，你可以在之后的这个时候输入：/open.bag，接下来输入；/use.UP来使用它')
                bag.append('强化药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    elif bywhat == 'c':
        if Money > 200:
            print('你确认要花费200¥购买恢复药水吗？a/b')
            passby = input()
            if passby == 'a':
                Money = Money - 200
                print('你购买了恢复药水，你可以在之后的这个时候输入：/open.bag，接下来输入；/use.BR来使用它')
                bag.append('恢复药水')
            elif passby == 'b':
                print('你不想购买它，你离开了商店')
            else:
                print('你离开了此地')
        else:
            print('Money不足')
    else:
        print('你离开了此地')


def job1():
    AC = 15
    HP = 10
    AB = 15
    QB = 8
    Money = 100
    land_list = ['宝库', '草地', '高山', '池塘', '火山', '黑森林', '森林',
                 '废墟', '神殿', '沙漠', '沼泽', '矿洞', '大海']  # 创立一个地点列表备用
    npc_list = ['一条幼年白龙', '一个哥布林', '一个巨人', '一个机器人', '一个骷髅']  # 创建一个人物列表备用
    attack_results = ['它攻击了你！你受伤了！', '你杀死了它！你赢了！',
                      '你杀死了它！你赢了！', '你杀死了它！你赢了！', '你杀死了它！你赢了！']
    # 为什么有重复？
    escape_results = ['它没有看到你的离开！你安然无恙！', '它攻击了你！你受伤了！',
                      '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', '它没有看到你的离开！你安然无恙！', ]
    hide_results = ['你没躲过它的攻击！你受伤了！', '它没有发现你，你成功逃过一劫！',
                    '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！', '它没有发现你，你成功逃过一劫！']
    # bag = []

    land_list_now = land_list[1:]
    for i in range(100000):
        if i >= 5:
            land_list_now = land_list
            # 让用户选择一个动作
        land = random.choice(land_list_now)
        if land == '宝库':
            # 如果选中宝库，那么，结束游戏
            print('Goodjob!你找到了宝库！智者告诉了你...(见下一部:Dranon Island II)')
            openlog = input()
            if openlog == '/log.makers':
                print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
                      'PRODUCTION DIRECTOR(制作总监):Eason', 'OPTIMIZATION DIRECTOR（优化总监）:Jason')
                time.sleep(2)
                print('Thanks For Playing! :D')
                time.sleep(2)
                sys.exit(0)
            else:
                sys.exit(0)
        # 设立一个语境，将随机选中的词语填充入内
        print('你进入了' + land + ',遇到了' + random.choice(npc_list))
        print('你要做什么？', '你可以选择：', '战斗', '逃避', '躲避', sep='\n')
        print('输入“a/b/c”来选择对应的动作')
        pc_movement = input().upper()

        while pc_movement not in ['A', 'B', 'C']:
            print('输入“a/b/c”来选择对应的动作')
            pc_movement = input().upper()

        if pc_movement == 'A':
            print('WOW！你选择了', '攻击！', '这可是勇者的行为！', 'Good Luck!', sep='\n')
            print('作为一名骑士，你可以使用你的巨剑(AB-1，QB-1)，或用你有力的拳头（HP-1）向敌人挥去（a/b）')
            attack_way = input().upper()
            if attack_way == 'A':
                print('你选择了使用巨剑攻击', '加油！', sep='\n')
                AB = AB - 1
                QB = QB + 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    HP = HP - random.randint(1, 3)
                    check()
                    print('你还剩下', HP, '点HP')
                    store()

                elif attack_instance == '你杀死了它！你赢了！':
                    Money = Money + random.randint(1, 50)
                    print(attack_instance, '你的战利品是金币，你现在有', Money, '个金币')
                    check()
                    print('你是否要进入商店？a/b')
                    passin = input()
                    if passin == 'a':
                        store()
            elif attack_way == 'B':
                print('你选择了使用拳头攻击', '加油', sep='\n')
                HP = HP - 1
                attack_instance = random.choice(attack_results)
                if attack_instance == '它攻击了你！你受伤了！':
                    print(attack_instance)
                    HP = HP - random.randint(1, 3)
                    check()
                    print('你还剩下', HP, '点HP')
                    store()
                elif attack_instance == '你杀死了它！你赢了！':
                    Money = Money + random.randint(1, 50)
                    print(attack_instance, '你的战利品是金币，你现在有', Money, '个金币')
                    check()
                    print('你是否要进入商店？a/b')
                    passin = input()
                    if passin == 'a':
                        store()
        elif pc_movement == 'B':
            print('WOW！你选择了', '逃避！', 'Good Luck!', sep='\n')
            print('作为一名骑士，你只能走着离开，按下任意一个键来继续下一步')
            input()
            QB = QB - 1
            HP = HP + 1
            escape_instance = random.choice(escape_results)
            if escape_instance == '它攻击了你！你受伤了！':
                print(escape_instance)
                HP = HP - random.randint(2, 4)
                check()
                print('你还剩下', HP, '点HP')
                store()
            elif escape_instance == '它没有看到你的离开！你安然无恙！':
                Money = Money + random.randint(1, 50)
                print(escape_instance, '你的战利品是金币，你现在有', Money, '个金币')
                check()
                print('你是否要进入商店？a/b')
                passin = input()
                if passin == 'a':
                    store()
        elif pc_movement == 'C':
            print('WOW！你选择了', '躲避！(AC-1,QB+1)', 'Good Luck!', sep='\n')
            print('作为一名骑士，你只能走着躲避，按下任意一个键来继续下一步')
            input()
            AC = AC - 1
            QB = QB + 1
            hide_instance = random.choice(hide_results)
            if hide_instance == '你没躲过它的攻击！你受伤了！':
                print(hide_instance)
                HP = HP - random.randint(2, 4)
                check()
                print('你还剩下', HP, '点HP')
                store()
            elif hide_instance == '它没有发现你，你成功逃过一劫！':
                Money = Money + random.randint(1, 50)
                print(escape_instance, '你的战利品是金币，你现在有', Money, '个金币')
                check()
                print('你是否要进入商店？a/b')
                passin = input()
                if passin == 'a':
                    store()
                    pass

def stage2():
    print('恭喜你闯过了第一关！', '不过你的路还很长，', '接下来你需要探索这座岛，',
          '找到宝库，也许智者会告诉你如何离开！', sep='\n')  # 简介
    time.sleep(2)
    # 选择职业
    print('首先，你得作出一个选择', '你要为自己选择一个职业', '一个没有职业的人，好比没有目标的炸弹',
          '你面前有三种选择', '战士，游侠与法师', '作出选择吧！（a/b/c）', sep='\n')
    job = input().upper()
    while job not in ['A', 'B', 'C']:
        print('输入“a/b/c”来选择对应的职业')
        job = input().upper()
    if job == 'a' or 'A':
        print('你选择了战士！', '这是一个不错的职业，只是…', '你首先要了解：', '我们的世界由五大属性组成：', sep='\n')
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
        print('当你了解了这些之后，你需要知道战士的各项属性', 'AC = 15', 'HP = 10', 'AB = 15',
              'QB = 8', 'Money = 100', '(任何一项为0，你都会死亡)', sep='\n')
        job1()


def helloplayer():
    print('欢迎来到', 'DRAGON ISLAND:FIRST START',
          '这部中文游戏由HACKER.C.D.GAME STUDIO开发制作.游玩愉快.')

# 显示游戏说明（1）


def display_intro():
    print('欢迎来到龙之岛.', '你眼前有两个山洞,', '里面分别有两条龙:一条温顺友好;一条凶恶残忍.',
          '选择权在你手中，自己作出选择吧！', sep='\n')

# 让用户选择一个洞穴

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':  # 如果用户写出了正确的洞穴，则跳出这个循环
        print('选择一个洞穴吧！(1或2)')
        cave = input()

    return cave


def checkCave():
    print('你进入了山洞...')
    time.sleep(2)

    seed = random.randint(1, 5)

    if seed <= 4:
        print('干的好...')
        time.sleep(2)
        print('你进入了温顺龙的洞穴！它给了你...')
        time.sleep(2)
        print('宝库的钥匙！\n')
        stage2()
    else:
        print('干的好...')
        time.sleep(2)
        print('你被凶恶龙一口吃了！oops!\n')


if __name__ == '__main__':
    playAgain = 'Yes'
    while playAgain == 'Yes' or playAgain == 'Y' or playAgain == 'y':  # 设立一个检测用户键入的程序
        display_intro()
        caveNumber = chooseCave()
        checkCave()

        print('想再来一局不？(Y or N)')
        playAgain = input()  # 检测键入