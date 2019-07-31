#Dranon Island
import random
import time
def cyy():#创立一个函数
    print('''恭喜你闯过了第一关！
不过你的路还很长，
接下来你需要探索这座岛，
找到宝库，也许智者会告诉你如何离开！''')#简介
    time.sleep(2)#等待2s
    land = ['草地','高山','池塘','火山','黑森林','森林','废墟','神殿','沙漠','沼泽','矿洞','大海','宝库' ] #创立一个地点列表备用
    thing = ['一条龙','一个哥布林','一个巨人','一个机器人']#创建一个人物列表备用
    Do = ['它攻击了你！你死了！','它走开了','它没看到你']#创立一个动作列表备用
    option = random.choice(land)#随机选择一个地点
    optionT = random.choice(thing)#随机选择一个人物
    DO = random.choice(Do)#随机选择一个动作

    while option != '宝库':#创立一个while循环，直到随机选中“宝库”
        print('你进入了' + option + ',遇到了' + optionT)#设立一个语境，将随机选中的词语填充入内
        print('你要做什么？(输入一个字符)')#让用户选择一个动作
        C = input()
        if C == ' ':
            print('???')
            break
        time.sleep(2)
        print(DO)#打印结果
        if DO == '它攻击了你！你死了！':
            print(DO)
            break
        option = random.choice(land)
        optionT = random.choice(thing)
        DO = random.choice(DO)#每次循环刷新一遍
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
while playAgain == 'Yes' or playAgain == 'Y':#设立一个检测用户键入的程序
    intro()
    caveNumber = chooseCave()
    checkCave(caveNumber)#执行步骤

    print('想再来一局不？(Yes or No)')#询问用户是否愿意再来一局
    playAgain = input()#检测键入

