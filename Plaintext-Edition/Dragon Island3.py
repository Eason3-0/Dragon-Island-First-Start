#Dragon Island v0.2.1
import random
import time
import sys
def cyy():#创立一个函数
    time.sleep(2)
    print('''恭喜你闯过了第一关！
不过你的路还很长，
接下来你需要探索这座岛，
找到宝库，也许智者会告诉你如何离开！''')#简介
    time.sleep(2)#等待2s
    land = ['草地','高山','池塘','火山','黑森林','森林','废墟','神殿','沙漠','沼泽','矿洞','大海','宝库' ] #创立一个地点列表备用
    landA = ['草地','高山','池塘','火山','黑森林','森林','废墟','神殿','沙漠','沼泽','矿洞','大海']
    thing = ['一条龙','一个哥布林','一个巨人','一个机器人']#创建一个人物列表备用
    todoa = ['它反击了你！你死了！','你杀死了它！你赢了！','你杀死了它！你赢了！','你杀死了它！你赢了！','你杀死了它！你赢了！']
    todob = ['它没有看到你的离开！你安然无恙！','它攻击了你！你死了！','它没有看到你的离开！你安然无恙！','它没有看到你的离开！你安然无恙！','它没有看到你的离开！你安然无恙！',]
    todoc = ['你没躲过它的攻击！你死了！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！','它没有发现你，你成功逃过一劫！']
    option = random.choice(land)#随机选择一个地点
    optionA = random.choice(landA)
    optionT = random.choice(thing)#随机选择一个人物
    optionTo = random.choice(todoa)
    optionToa = random.choice(todob)
    optionTob = random.choice(todoc)   

    for _ in range(5) :#创立一个for循环
        print('你进入了' + optionA + ',遇到了' + optionT)#设立一个语境，将随机选中的词语填充入内
        print('你要做什么？(输入：攻击/逃开/躲避/自杀或a/b/c/d(小写))')#让用户选择一个动作
        C = input()
        if C == '自杀' or C == 'd':
            print('你死了！')
            sys.exit(0)
        elif C == '攻击' or C == 'a':
            time.sleep(2)
            print(optionTo)#打印结果
            if optionTo == '它反击了你！你死了！':
                sys.exit(0)
        elif C == '逃开' or C == 'b':
            time.sleep(2)
            print(optionToa)
            if optionToa == '它攻击了你！你死了！':
                sys.exit(0)
        elif C == '躲避' or C == 'c':
            time.sleep(2)
            print(optionTob)
            if optionTob == '你没躲过它的攻击！你死了！':
                sys.exit(0)
        option = random.choice(land)
        optionT = random.choice(thing)
        optionTo = random.choice(todoa)
        optionToa = random.choice(todob)
        optionTob = random.choice(todoc) 
    
    while option != '宝库':#创立一个while循环，直到随机选中“宝库”
        print('你进入了' + option + ',遇到了' + optionT)#设立一个语境，将随机选中的词语填充入内
        print('你要做什么？(输入：攻击/逃开/躲避/自杀或a/b/c/d(小写))')#让用户选择一个动作
        C = input()
        if C == '自杀':
            print('你死了！')
            sys.exit(0)
        elif C == '攻击':
            time.sleep(2)
            print(optionTo)#打印结果
            if optionTo == '它反击了你！你死了！':
                sys.exit(0)
        elif C == '逃开':
            time.sleep(2)
            print(optionToa)
            if optionToa == '它攻击了你！你死了！':
                sys.exit(0)
        elif C == '躲避':
            time.sleep(2)
            print(optionTob)
            if optionTob == '你没躲过它的攻击！你死了！':
                sys.exit(0)
        option = random.choice(land)
        optionT = random.choice(thing)
        optionTo = random.choice(todoa)
        optionToa = random.choice(todob)
        optionTob = random.choice(todoc) 
    
    if option == '宝库':
        print('Goodjob!你找到了宝库！智者告诉了你...(见下一部:Dranon Island II)')#如果选中宝库，那么，结束游戏

def intro():
    print('''欢迎来到龙之岛.
你眼前有两个山洞,
里面分别有两条龙:一条温顺友好;一条凶恶残忍.
选择权在你手中，自己作出选择吧！''')
    print()#设置开始句

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('选择一个洞穴吧！(1或2)')
        cave = input()#让用户选择一个洞穴

    return cave#如果用户写出了正确的洞穴，则跳出这个循环

def checkCave(chosenCave):
    print('你进入了山洞...')
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print('干的好...')
        time.sleep(2)
        print('你进入了温顺龙的洞穴！它给了你...')
        time.sleep(2)
        print('''宝库的钥匙！
 ''')
        cyy() 
    else:
        print('干的好...')
        time.sleep(2)
        print('''你被凶恶龙一口吃了！oops!
 ''')
        #设置两种情况

playAgain = 'Yes'
while playAgain == 'Yes' or playAgain == 'Y' or playAgain == 'y':#设立一个检测用户键入的程序
    intro()
    caveNumber = chooseCave()
    checkCave(caveNumber)#执行步骤

    print('想再来一局不？(Y or N)')#询问用户是否愿意再来一局
    playAgain = input()#检测键入

