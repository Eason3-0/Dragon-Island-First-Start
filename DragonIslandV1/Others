land_list = ['宝库', '草地', '高山', '池塘', '火山', '黑森林', '森林',
            '废墟', '神殿', '沙漠', '沼泽', '矿洞', '大海']  # 创立一个地点列表备用


def display_cookie_for_input():
    openlog = input()
    if openlog == '/log.makers':
        print('HACKER.C.D.GAME STUDIO', 'GAME MAKERS:',
            'PRODUCTION DIRECTOR(制作总监):Eason Chen', 'OPTIMIZATION（代码总监）:Jason Chen',
            'ORIGINALITY FROM(创意来源):Chloe Zhao&Wind Is blowing Li&Amy Wu'sep='\n')
        time.sleep(2)
        print('Thanks For Playing our Game! :D')
        time.sleep(2)
        sys.exit(0)
    else:
        print('Thanks For Playing our Game! :D')
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

def display_copyright():
    print('~~~~欢迎到来~~~~', 'DRAGON ISLAND: FIRST START', 
    '这部中文游戏由HACKER.C.D.GAME STUDIO开发制作.游玩愉快.','按下回车键以开始游戏','—'*60, sep='\n')
    openEgg = input()
    if openEgg == '/Egg.open':
        Egg()
    else:
        print('游戏开始','-'*60,sep='\n')

# 显示游戏说明（1）
def display_game_introduce():
    print('欢迎来到龙之岛.', '你眼前有两个山洞,', '里面分别有两条龙:一条温顺友好;一条凶恶残忍.',
          '选择权在你手中，自己作出选择吧！', sep='\n')

def go_store(player):
    print('现在是购买环节，你可以购买：', '生命药水——帮你恢复3点的HP',
          '强化药水——帮你恢复1点的AC与2点的AB', '恢复药水——帮你恢复1点HP与2点的QB', sep='\n')
    print(f'以下为你的各项点数：AC: {player.AC}, HP: {player.HP}, QB: {player.QB}, Money: {player.Money}')
    bywhat = input('你要买什么呢？以上的药水价格分别为150M/200M/200M/使用背包中的药水（a/b/c/代码）')
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
        print('你离开了商店')

def create_role():
    print('恭喜你闯过了第一关！', '不过你的路还很长，', '接下来你需要探索这座岛，','这座离奇，又充满着神秘气息的岛屿……',
          '找到宝库，也许看守着宝库的智者会告诉你如何离开！', sep='\n')  # 简介
    
    time.sleep(2)

    # 选择职业
    option = input('首先，你得作出一个选择\n你要为自己选择一个职业\n一个没有职业的人，好比没有目标的炸弹\n你面前有三种选择\n战士、法师与游侠\n作出你的选择吧！（a/b/c）').lower()
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
    monster_cls_list = [Monster_YoungWhiteDragon, Monster_BlzingSkeleton, Monster_DecrepitSkeleton, Monster_GoblinCutter,Monster_GoblinHexer]
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

                escaped = False            
                while True:
                    if monster.QB > role.QB:
                        monster.do_fight_round(role)
                        if (not monster.is_alive()) or (not role.is_alive()):
                            break

                        escaped = role.do_fight_round(monster)
                        if escaped or (not monster.is_alive()) or (not role.is_alive()):
                            break
                    else: # role.QB >= monster.QB
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