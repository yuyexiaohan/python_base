# coding=utf-8 
# Time : 2019/2/14
# Author : achjiang
"""
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
# 1. python自带的方法：split切割，使用join拼接
# 2.

class Solution():
    # s 源字符串/推荐python特有方法
    def replaceSpace(self, s):
        # write code here
        return "%20".join(list(s.split (" ")))


class Solution1():
	# s 源字符串/原始方法
	def replaceSpace(self, s):
		# write code here
		# 1.判断是否是字符串/长度是否为0/是否为空
		if not isinstance (s, str) or len (s) <= 0 or s == None:
			return ''
		spaceNum = 0
		# 2.遍历字符串，统计空格数量
		for i in s:
			if i == " ":
				spaceNum += 1
		# 3.计算新字符串长度
		newStrLen = len (s) + spaceNum * 2
		newStr = newStrLen * [None]
		print("newstr:", newStr)
		indexOfOriginal, indexOfNew = len (s) - 1, newStrLen - 1
		while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
			if s[indexOfOriginal] == ' ':
				newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
				indexOfNew -= 3
				indexOfOriginal -= 1
			else:
				newStr[indexOfNew] = s[indexOfOriginal]
				indexOfNew -= 1
				indexOfOriginal -= 1
		return ''.join (newStr)

# ss = Solution()
ss = Solution1()
str1 = ss.replaceSpace('123   ###12 we ')
str2 = ss.replaceSpace('123###12we')
print(str1)
print(str2)