# coding=utf-8 
# @Time : 2018/9/6 22:17 
# @Author : achjiang
# @File : algorithm_04斐波那契数列.py

# 斐波那契数列的写法：f(0) = 1,f(1) = 1,f(n) = f(n-1) + f(n-2)

# 方法1：使用递归调用的方法
def fibonacci_numbers_unit(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci_numbers_unit(n - 1) + fibonacci_numbers_unit(n - 2)

def fibonacci_numbers_01(n):
	fibonacci_list = []
	for i in range(0,n + 1):
		fibonacci_list.append(fibonacci_numbers_unit(i))
	return fibonacci_list

a = fibonacci_numbers_01(5)
# print(type(a),a)
# 打印结果：
# <class 'list'> [0, 1, 1, 2, 3, 5]

# 方法2：循环法
def finonacci_loop(n):
	fibonacci_list = []
	a, b = 0, 1
	while n > 0:
		fibonacci_list.append(b)
		a, b = b, a + b
		n -= 1
	return fibonacci_list
b = finonacci_loop(5)
print(b)





