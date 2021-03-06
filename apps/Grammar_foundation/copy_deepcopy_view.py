# coding=utf-8 
# @Time : 2018/8/21 15:23 
# @Author : achjiang
# @File : copy_deepcopy_view.py

'''python基础语法练习'''
# 1.深拷贝和浅拷贝
# 浅拷贝
# 是在另一块地址中创建一个新的变量或容器，但是容器内的元素的地址均是源对象的元素的地址的拷贝。也就是说新的容器中指向了旧的元素（ 新瓶装旧酒 ）。

#首先，对赋值操作我们要有以下认识：
#赋值是将一个对象的地址赋值给一个变量，让变量指向该地址（ 旧瓶装旧酒 ）。
#修改不可变对象（str、tuple）需要开辟新的空间
#修改可变对象（list等）不需要开辟新的空间

# 深拷贝
#是在另一块地址中创建一个新的变量或容器，同时容器内的元素的地址也是新开辟的，仅仅是值相同而已，是完全的副本。也就是说（ 新瓶装新酒 ）。

# 具体例子如下：

import copy
a = [1, 2, 3, 4, ['a', 'b']]  #原始对象
print ('a = ', a,'\n', 'id(a):',id(a))

print('-----------原始对象各元素地址----------')
for i in a:
	print('%s:'%i,'id:(%s)'%id(i))

b = a  #赋值，传对象的引用
c = copy.copy(a)  #对象拷贝，浅拷贝
print('-----------浅拷贝后各元素地址----------')
for m in c:
	print('%s:'%m,'id:%s'%id(m))
print('-----------深拷贝后各元素地址----------')
d = copy.deepcopy(a)  #对象拷贝，深拷贝
for n in d:
	print('%s:'%n,'id:%s'%id(n))

a.append(5)  #修改对象a
a[4].append('c')  #修改对象a中的['a', 'b']数组对象

print('-----------原始变量改变后，浅拷贝对象的各元素地址----------')
for m in c:
	print('%s:'%m,'id:%s'%id(m))
print('-----------原始变量改变后，深拷贝对象的各元素地址----------')
for n in d:
	print('%s:'%n,'id:%s:'%id(n))


print ('a = ', a,'\n', 'id(a):',id(a))
print ('b = ', b,'\n','id(b):',id(b))
print ('c = ', c,'\n','id(c):',id(c))
print ('d = ', d,'\n','id(d):',id(d))
'''
输出结果：
 # 最初的a,
 a =  [1, 2, 3, 4, ['a', 'b']] 
 id(a): 2215279651016
#  每一个元素的地址，可以发现，对于不可变量（str,tuple,num）的地址是不变的;但是对于可变变量（list,dict）浅拷贝是不变的，但是深拷贝就赋予该类型变量一个新的地址。
-----------原始对象各元素地址----------
1: id:1710535744
2: id:1710535776
3: id:1710535808
4: id:1710535840
['a', 'b']: id:2215531253256
-----------浅拷贝后各元素地址----------
1: id:1710535744
2: id:1710535776
3: id:1710535808
4: id:1710535840
['a', 'b']: id:2215531253256
-----------深拷贝后各元素地址----------
1: id:1710535744
2: id:1710535776
3: id:1710535808
4: id:1710535840
['a', 'b']: id:2215279696456
-----------原始变量改变后，浅拷贝对象的各元素地址----------
1: id:1710535744
2: id:1710535776
3: id:1710535808
4: id:1710535840
['a', 'b', 'c']: id:2215531253256

 # 浅拷贝只是拷贝了当时a的地址，所以当对a添加了‘5’时，其实a的地址已经变化了
-----------原始变量改变后，深拷贝对象的各元素地址----------
1: id:1710535744
2: id:1710535776
3: id:1710535808
4: id:1710535840
['a', 'b']: id:2215279696456

 # 此时的a本身
a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5] 
 id(a): 2215279651016 id(a[5]): 1710535872
 
  # b地址指向a
b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5] 
 id(b): 2215279651016
 # c 浅拷贝的变量地址发生变化，不包含a中的元素5.说明浅拷贝只是拷贝了a变量的元素地址，当a中增加或减少元素时，该变量的地址也会发生变化。
c =  [1, 2, 3, 4, ['a', 'b', 'c']] 
 id(c): 2215279695112
 
d =  [1, 2, 3, 4, ['a', 'b']] 
 id(d): 2215279650120
'''






