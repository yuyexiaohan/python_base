# coding=utf-8 
# @Time : 2018/8/31 14:31 
# @Author : achjiang
# @File : time_1.py

#

import re,time
class NextSecond():
	def next_seconf(self,str):
		s_list=re.findall("\d+",str) # 正则查找素有匹配0~9的数值，‘+’多次，返回一个list
		s="".join(s_list)
		# 将数据转换为time.struct_time(tm_year=2017, tm_mon=12, tm_mday=17, tm_hour=18, tm_min=18, tm_sec=18, tm_wday=6, tm_yday=351, tm_isdst=-1)
		strptime=time.strptime(s,"%Y%m%d%H%M%S")
		timestamp=time.mktime(strptime) #time.mktime把struct_time转成时间戳:1510242839.0
		# print(timestamp)
		new_timestamp=timestamp+1
		new_str=time.localtime(new_timestamp) #
		dt=time.strftime("%Y-%m-%d %H:%M:%S", new_str) # 将struct_timeh函数转换为指定格式的字符串
		dt_list=re.findall("\d+", dt)
		return "%s年%s月%s日%s时%s分%s秒"%(dt_list[0],dt_list[1],dt_list[2],dt_list[3],dt_list[4],dt_list[5])

if __name__=='__main__':
	a = NextSecond()
	print (a.next_seconf("2017年11月09日23时53分59秒"))
	print (a.next_seconf("2004年12月31日23时59分59秒"))

	print (time.strptime ('2017-12-17 18:18:18', '%Y-%m-%d %H:%M:%S'))