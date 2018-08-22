# coding=utf-8 
# @Time : 2018/8/22 11:05 
# @Author : achjiang
# @File : generators_filtrators_decorators_iterators.py

# 2.装饰器、生成器(generators)、迭代器(iterator)、过滤器(filtrator)


# 装饰器(decorators)
# 1 不带参数的装饰器
import time
def timmer(func):
 def wrapper():
  """计时功能"""
  time_start=time.time()
  func()
  time_end=time.time()
  print("Run time is %f "%(time_end-time_start))
 return wrapper
@timmer  #等于 foo=timmer(foo)
def foo():
 """打印"""
 time.sleep(2)
 print("Hello boy!")
foo()

# 打印结果：
# Hello boy!
# Run time is 2.000000

# 从结果看，先执行

# 2 带参数的装饰器
def auth(filetype):
 def auth2(func):
  def wrapper(*args,**kwargs):
   if filetype == "file":
    username=input("Please input your username:")
    passwd=input("Please input your password：")
    if passwd == '123456' and username == 'Frank':
     print("Login successful")
     func()
    else:
     print("login error!")
   if filetype == 'SQL':
    print("No SQL")
  return wrapper
 return auth2
@auth(filetype='file') #先先返回一个auth2 ==》@auth2 ==》 index=auth2(index) ==》 index=wrapper
def index():
 print("Welcome to China")
index()

# 打印结果：
# 输入错误情况：
# Please input your username:123
# Please input your password：123
# login error!

# 输入正确情况：
# Please input your username:Frank
# Please input your password：123456
# Login successful
# Welcome to China

# 3 装饰器的叠加：

import time
#
def timmer(func):
 def wrapper():
  """计时功能"""
  time_start=time.time()
  func()
  time_end=time.time()
  print("Run time is %f "%(time_end-time_start))
  # print("---",wrapper)
 return wrapper
def auth(filetype):
 def auth2(func):
  def wrapper(*args,**kwargs):
   if filetype == "file":
    username=input("Please input your username:")
    passwd=input("Please input your password：")
    if passwd == '123456' and username == 'Frank':
     print("Login successful")
     func()
    else:
     print("login error!")
   if filetype == 'SQL':
    print("No SQL")
  return wrapper
 return auth2
@timmer
@auth(filetype='file') #先先返回一个auth2 ==》@auth2 ==》 index=auth2() ==》 index=wrapper
def index():
 print("Welcome to China")
index()

# 打印结果：
#Please input your username:Frank
# Please input your password：123456
# Login successful
# Welcome to China
# Run time is 12.507478

#

# 生成器(generators)/迭代器(iterator)

### 生成器和列表推导式之前的差别
# - 生成器和迭代器的区别就是用()代替[],
# - 通过列表生成式，可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含百万元素的列表，不仅是占用很大的内存空间，如：我们只需要访问前面的几个元素，后面大部分元素所占的空间都是浪费的。因此，没有必要创建完整的列表（节省大量内存空间）。在Python中，我们可以采用生成器：边循环，边计算的机制—>generator
# - 你不能用for i in generator第二次调用生成器，因为生成器是:首先计算0,然后会在内存里丢掉0去计算2,直到计算完4

L = [x*2 for x in range(10)]
print('L=',L)
for i in L:
	print('i:',i)
# 打印结果
# L= [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# i: 0
# i: 2
# i: 4
# i: 6
# i: 8
# i: 10
# i: 12
# i: 14
# i: 16
# i: 18


G = (x*2 for x in range(10)) # 将列表推导式的中括号，变成小括号，对于的值就变成了生成器
print('G=',G)
for m in G:
	print('m:',m)

print('--------第二次调用生成器---------')

print('G=',G)
for n in G:
	print('n:',n) # 实际无输出
# 打印结果
# G= <generator object <genexpr> at 0x0000024A66A02B48>

# i: 0
# i: 2
# i: 4
# i: 6
# i: 8
# i: 10
# i: 12
# i: 14
# i: 16
# i: 18
# --------第二次调用生成器---------
# G= <generator object <genexpr> at 0x0000029D4A042B48>



# 过滤器


# 3.yield
import itertools










