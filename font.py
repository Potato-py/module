#!/usr/bin/python
# -*- coding:utf-8

#引用对象需添加以下code：
#------------------------appendPath------------------------
#自定义目录使用sys.path.append(sys.path[0]+r'../common')
#上层目录使用sys.path.append('..')
#当前目录下可忽略添加环境地址
#--------------------------import--------------------------
#from common.font import *
#-------防止高频调用导致堵塞，可对某些字段进行存储---------
#Processing=str(Processing())
#Information=str(Information())
#Detected=str(Detected())
#Result=str(Result())
#Error=str(Error())

import os
import sys

try:
    import terminal
except:
    print('检测出您未安装terminal模块，将替您安装此模块，请稍候……')
    os.system('pip3 install terminal')
    import terminal
try:
    import console
except:
    print('检测出您未安装console模块，将替您安装此模块，请稍候……')
    os.system('pip3 install console')
    import console

#
# color方法
#
def red(text):
    return terminal.bold(terminal.red(text))

def green(text):
    return terminal.green(text)

def blue(text):
    return terminal.bold(terminal.blue(text))

def magenta(text):
    return terminal.magenta(text)

def yellow(text):
    return terminal.yellow(text)

def cyan(text):
    return terminal.cyan(text)

def bold(text):#高亮
    return terminal.bold(text)

def Processing():
    return terminal.magenta(r"[Processing] ")

def Information():
    return terminal.cyan(r"[Information] ")

def Detected():
    return terminal.bold(terminal.blue(r"[Detected] "))

def Result():
    return terminal.bold(terminal.green(r"[Result] "))

def Error():
    return terminal.bold(terminal.red(r"[Error] "))

def Input(*num):
    if(num and num[0]!= 1):
        data = r"<Potato>- "
    else:
        data = r"<Potato>$ "
    return terminal.bold(terminal.yellow(data))

#实现回车换行，而不是结束
def Input_lines():
    result = ""
    num = 0
    while True:
        num = num + 1
        data = str(input(Input(num)))
        if data == '':
            if(num==1):
                print(Error()+'首行不能为空，请重新输入！\n')
                result = ""
                num = 0
                continue
            return result
        result+= data+"\n"#换行


#格式化输出
def printF(strData, lenMax, placeHolder=" ", justify="center"):
    strData = str(strData)
    lenChina = 0
    for i in strData:
        lenChina+=1 if i not in string.printable else 0
    return strData.center(lenMax-lenChina,placeHolder) if justify=="center" else strData.ljust(lenMax-lenChina,placeHolder) if justify=="left" else strData.rjust(lenMax-lenChina,placeHolder)

#调用直接打印table
# printT( [8,13,13,10] ,"top")
# printT( [["ip",8],["域名",13,"left"],["权重",13,"center"],["编号",10]])
# printT( [8,13,13,10] ,"middle")
# printT( [["ip",8],["域名",13,"left"],["权重",13],["编号",10]],type="body")
# printT( [8,13,13,10] ,"bottom")
#tableStyle、fontStyle 分别控制字体和表格颜色
def printT(dataList,type="body",getStr=False,tableStyle="red",fontStyle=""):

    def table(str):
        if tableStyle == "red":
            return red(str)
        elif tableStyle == "green":
            return green(str)
        elif tableStyle == "magenta":
            return magenta(str)
        elif tableStyle == "blue":
            return blue(str)
        elif tableStyle == "yellow":
            return yellow(str)
        elif tableStyle == "cyan":
            return cyan(str)
        elif tableStyle == "bold":
            return bold(str)
        else:
            return str

    def font(str):
            if fontStyle == "red":
                return red(str)
            elif fontStyle == "green":
                return green(str)
            elif fontStyle == "magenta":
                return magenta(str)
            elif fontStyle == "blue":
                return blue(str)
            elif fontStyle == "yellow":
                return yellow(str)
            elif fontStyle == "cyan":
                return cyan(str)
            elif fontStyle == "bold":
                return bold(str)
            else:
                return str

    try:
        str=""
        if type == "top":
            str = table("┌")
            for index, data in enumerate(dataList):
                str += table("─" * data)
                str += table("┬") if index != len(dataList)-1 else table("┐")
        elif type == "bottom":
            str = table("└")
            for index, data in enumerate(dataList):
                str += table("─" * data)
                str += table("┴") if index != len(dataList)-1 else table("┘")
        elif type == "middle":
            str = table("├")
            for index, data in enumerate(dataList):
                str += table("─" * data)
                str += table("┼") if index != len(dataList)-1 else table("┤")
        else:
            str = table("│")
            for data in dataList:
                justify = "center" if len(data)==2 else data[2]
                str += f"{font(printF(data[0], data[1], justify=justify))}{table('│')}"
        if getStr:
            return str
        else:
            print(str)
    except Exception as e:
        print(f"\033[31m[Error] {e}\r\n")
        print('正确使用方法：')
        print('    printT( [8,13,13,10] ,"top")')
        print('    printT( [["ip",8],["域名",13,"left"],["权重",13],["编号",10]])')
        print('    printT( [8,13,13,10] ,"middle")')
        print('    printT( [["ip",8],["域名",13,"left"],["权重",13],["编号",10]])')
        print('    printT( [8,13,13,10] ,"bottom")\033[0m')

#
# logo打印
#
def logo_1():
    os.system("cls") if ('win' in sys.platform and 'darwin' not in sys.platform) else os.system("clear")
    print ('')
    print ('''\033[1m

############################################################################################
##                           \033[0m'''+'''\033[1;31m    ___       ___       ___       ___       ___       ___    \033[0m'''+'''\033[1m##
##  --ScriptName: potato     \033[0m'''+'''\033[1;31m   /\  \     /\  \     /\  \     /\  \     /\  \     /\  \   \033[0m'''+'''\033[1m##
##  --Author    : LiJunYi    \033[0m'''+'''\033[1;31m  /::\  \   /::\  \    \:\  \   /::\  \    \:\  \   /::\  \  \033[0m'''+'''\033[1m##
##  --QQ        : 2438325121 \033[0m'''+'''\033[1;34m /:\033[0m'''+'''\033[1;31m:\:\__\ \033[0m'''+'''\033[1;34m/:\033[0m'''+'''\033[1;31m/\:\__\   /::\__\ \033[0m'''+'''\033[1;34m/:\033[0m'''+'''\033[1;31m:\:\__\   /::\__\ \033[0m'''+'''\033[1;34m/:\033[0m'''+'''\033[1;31m/\:\__\ \033[0m'''+'''\033[1m##
##  --Type      : Penetration\033[0m'''+'''\033[1;34m \/\\\033[0m'''+'''\033[1;31m::/  / \033[0m'''+'''\033[1;34m\:\\\033[0m'''+'''\033[1;31m/:/  /  \033[0m'''+'''\033[1;34m/:\033[0m'''+'''\033[1;31m/\/__/ \033[0m'''+'''\033[1;34m\/\\\033[0m'''+'''\033[1;31m::/  /  \033[0m'''+'''\033[1;34m/:\033[0m'''+'''\033[1;31m/\/__/ \033[0m'''+'''\033[1;34m\:\\\033[0m'''+'''\033[1;31m/:/  / \033[0m'''+'''\033[1m##
##  --Version   : 0.2.4      \033[0m'''+'''\033[1;34m    \\\033[0m'''+'''\033[1;31m/__/   \033[0m'''+'''\033[1;34m\::\033[0m'''+'''\033[1;31m/  /   \033[0m'''+'''\033[1;34m\/__/      /:\033[0m'''+'''\033[1;31m/  /   \033[0m'''+'''\033[1;34m\/__/     \::\033[0m'''+'''\033[1;31m/  /  \033[0m'''+'''\033[1m##
##                           \033[0m'''+'''\033[1;34m             \/__/               \/__/               \/__/   \033[0m'''+'''\033[1m##
############################################################################################

\033[0m''')

def logo_2():
    print(red('''
                     __        __      
        ____  ____ _/ /_____ _/ /_____ 
       / __ \/ __ `/ __/ __ `/ __/ __ \ 
      / /_/ / /_/ / /_/ /_/ / /_/ /_/ / ''')+blue(''' 
     / .___/\____/\__/\__,_/\__/\____/ 
    /_/  
'''))