import random
import time
import sys

def stage2():
    time.sleep(2)
    print('恭喜你闯过了第一关！', '不过你的路还很长，', '接下来你需要探索这座岛，', '找到宝库，也许智者会告诉你如何离开！', sep='\n') # 简介
    time.sleep(2)

    land_list = ['宝库', '草地', '高山', '池塘', '火山', '黑森林', '森林', '废墟', '神殿', '沙漠', '沼泽', '矿洞', '大海']  # 创立一个地点列表备用
    npc_list = ['一条龙','一个哥布林','一个巨人','一个机器人'] # 创建一个人物列表备用
    attack_results = ['它反击了你！你死了！','你杀死了它！你赢了！','你杀死了它！你赢了！','你杀死了它！你赢了！','你杀死了它！你赢了！']
    escape_results = ['它没有看到你的离开！你安然无恙！','它攻击了你！你死了！','它没有看到你的离开！你安然无恙！','它没有看到你的离开！你安然无恙！','它没有看到你的离开！你安然无恙！',]
    hide_results = ['你没躲过它的攻击！你死了！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！']
    
    land_list_now = land_list[1:]
    for i in range(100000):
        if i >= 5:
            land_list_now = land_list
            
        land = random.choice(land_list_now)
        print('你进入了' + land + ',遇到了' + random.choice(npc_list))  # 设立一个语境，将随机选中的词语填充入内
        print('你要做什么？(输入：攻击/逃开/躲避/自杀或a/b/c/d(小写))')#让用户选择一个动作
        action = input()
        if action == '自杀' or action == 'd':
            print('你死了！')
            return
        elif action == '攻击' or action == 'a':
            time.sleep(2)
            result = random.choice(attack_results)
            print(result)  # 打印结果
            if result == '它反击了你！你死了！':
                return
        elif action == '逃开' or action == 'b':
            time.sleep(2)
            result = random.choice(escape_results)
            print(result) 
            if result == '它攻击了你！你死了！':
                return
        elif action == '躲避' or action == 'c':
            time.sleep(2)
            result = random.choice(hide_results)
            print(result)
            if result == '你没躲过它的攻击！你死了！':
                return
    
        if land == '宝库':
            print('Goodjob!你找到了宝库！智者告诉了你...(见下一部:Dranon Island II)')  #如果选中宝库，那么，结束游戏
            sys.exit(0)

# 显示游戏说明（1）
def display_intro():
    print('欢迎来到龙之岛.', '你眼前有两个山洞,', '里面分别有两条龙:一条温顺友好;一条凶恶残忍.', '选择权在你手中，自己作出选择吧！', sep='\n')
    print()

# 让用户选择一个洞穴
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2': # 如果用户写出了正确的洞穴，则跳出这个循环
        print('选择一个洞穴吧！(1或2)')
        cave = input()

    return cave 

def checkCave():
    print('你进入了山洞...')
    time.sleep(2)

    seed = random.randint(1,5)

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
    while playAgain == 'Yes' or playAgain == 'Y' or playAgain == 'y': # 设立一个检测用户键入的程序
        display_intro()
        caveNumber = chooseCave()
        checkCave()

        print('想再来一局不？(Y or N)')
        playAgain = input() # 检测键入