# coding=utf-8 
# @Time : 2018/8/23 16:17 
# @Author : achjiang
# @File : change_or_unchange.py

#python里的数据类型:  数值类型（int,float,complex,bool）/序列类型 （str list tuple）

#数值类型

    #整型 int    整数  正整数 负整数 0
#a=1

    #浮点型  float   带有小数点的就是浮点型
#b=1.2
           #内置函数  type() 查看对象的类型

    #复数  complex
#c=1+2j   #可以是大写。   了解一下。 数学

    #布尔值  bool   True(1) False(0)

#序列类型  字符串str  列表list  元组tuple
#有顺序的数据类型 --->序列类型
    #str:  用引号包裹起来的就是字符串  '1' "1" '''1''' """1"""
    #三引号可以换行

    #list是用[]括起来的数据类型
    #list的定义:li=[]   li1=[1,2,3]
a=None
li = [True,False,None]
    #tuple
    #tuple的定义：t=()  t1=(None,1,'helloworld')
    #如何定义只有一个元素的元组？ t1=(1,)

#序列类型的取值
    #索引取值   索引值是从0开始的
        #正索引   0,1,2,3,4  从左到右
        #负索引   -1，-2，-3  从右到左
#li=[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a']
    #切片取值 li[1:7] li[1:8]
        #切片是左闭右开   左边的1会取到 而右边的端值不会取到

        #步长 li[0:5:1] li[0:5:2]
            #正步长 从左到右
            #负步长 从右到左
        # li[:]  li[::]


# python 中数据类型的可变和不可变

# 不可变的数据类型：tuple,string,number
# 可变的数据类型： list,dict