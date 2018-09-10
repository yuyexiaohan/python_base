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
# print(b)
# 打印结果：
# [1, 1, 2, 3, 5]

# 方法3：yield方法,生成器的方法
def fibonacci_yield(n):
	a, b = 0, 1
	while n:
		yield b
		a, b = b, a + b
		n -= 1

def fibonacci_yield_01(n):
	return list(fibonacci_yield(n))
c = fibonacci_yield_01(5)
# print(c)
# 打印结果：
# [1, 1, 2, 3, 5]


# 第4种方法：矩阵，暂时未理解
import numpy as np
# 矩阵
Matrix = np.matrix('1 1;1 0')
# 其n-1 次方的第一位,也就是Matrix(11)--下标11就是斐波那契数列的解

def Fibonacci_Matrix_tool(n): # 递归求解,速度慢与直接求方
    Matrix = np.matrix('1 1;1 0')
    if n == 1:
        return Matrix
    if n == 2:
        return pow(Matrix, 2)
    elif n % 2 == 1:
        return Fibonacci_Matrix_tool((n - 1) / 2) ** 2 * Matrix
    else:
        return Fibonacci_Matrix_tool(n / 2) ** 2


def Fibonacci_Matrix_tool2(n):
    Matrix = np.matrix('1 1;1 0')
    return pow(Matrix, n) # pow函数速度快于 使用双星号 "**"


def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n): result_list.append(np.array(Fibonacci_Matrix_tool2(i))[0][0])
    return result_list

d = Fibonacci_Matrix(5)
print(d)


# 第5种，斐波那契数列的扩展，青蛙跳
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
    # 青蛙跳台阶, 每次可以跳1级或2级
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]

    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

test = Solution()
print(test.Fibonacci(100))
print(test.jumpFloor(3))
print(test.jumpFloorII(2))
