# coding=utf-8
# @Time : 2018/9/3 22:40 
# @Author : achjiang
# @File : algorithm_02前n项的和.py

'''
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
import datetime
# 方法1：求前n项和
class Solution:

    def Sum_Solution(self, n):
        return self.sumN(n)

    def sum0(self, n):
        return 0

    # 利用非0值作两次非运算返回false, 0作两次非运算返回True
    def sumN(self, n):
        fun = {False: self.sum0, True: self.sumN}
        # 此处的fun[not not n] 不能写作func[not not n-1], 否则测试用例为0的话, 就会无限次迭代
        return n + fun[not not n](n - 1)

    def Sum_Solution2(self, n):
        return n and self.Sum_Solution(n - 1) + n
star_time = datetime.datetime.now()
s = Solution()
print('***计算前n项的和***')
# n = int(input('请输入n值(注意n值必须为正整数):'))
n = 3
print('前 %s 项的和为：'%n,s.Sum_Solution(n))
end_time = datetime.datetime.now()
print('程序运行时间是：',end_time-star_time)
# 方法2：求前n项和

class Sum_n:
	def sum_n(self,n):
		if n == 0:
			return 0
		else:
			return n + self.sum_n(n-1)
star_time = datetime.datetime.now()
s = Sum_n()
# n = int(input('请输入一个n值（n为正整数）：'))
n = 3
print('前%s项的和为：'%n,s.sum_n(n))
end_time = datetime.datetime.now()
print('程序运行时间是：',end_time-star_time)