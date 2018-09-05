# coding=utf-8 
# @Time : 2018/9/5 12:35 
# @Author : achjiang
# @File : re_test.py

"""正则练习"""
# 完成邮箱/网址url的正则匹配

"""
1.匹配邮箱
要求：
-- 输入是什么？字符串
-- 输出是什么？匹配的邮箱/检验输入邮箱是否合法
分析：从邮箱结构入手，邮箱一般分为四个部分
-- 邮箱文本:由字母、数字、下划线
-- @
-- 邮箱服务商（域名）：一般是字母、数字
-- .com/.net等：多为字母
2.网址匹配：
分析：
-- 匹配网页的url即在网页源代码中回去url
-- 匹配多为a标签中的href='url'标签内容,
-- 

"""
import re
'''
def match_email():
	"""邮箱正则匹配"""
	email_addr = input('请输入你的邮箱地址：')

	# 方法1：
	# 匹配单个邮箱：
	str = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+$'
	# 匹配多个邮箱
	str = r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+'

	# 指定分组部分测试
	# 匹配单个邮箱，分组匹配
	str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
	# 匹配多个邮箱，分组匹配：
	str = r'([a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){1,4})'
	# 输入：123 123@163.com asd qwe !24@ QAZwsx1@_123.net
	# 打印结果：[('123@163.com', '', '.com'), ('QAZwsx1@_123.net', '', '.net')]

	# 方法2：
	# 匹配单个邮箱：
	# str = r'^[\w-]+@[\w-]+\.[\w-]+$'
	# str = r'^([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)$'
	# 匹配多个邮箱：
	# str = r'[\w-]+@[\w-]+\.[\w-]+'

	# 指定分组测试：
	# 分组匹配,必须所有的括号内的正则表达试都匹配才会返回值，否则返回未None
	str = r'([\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+)'
	# 打印结果：[('123@163.com', ''), ('QAZwsx1@_123.net', '')]
	str = r'([\w-]+(\.[\w-]+)*@[\w-]+\.[\w-]+)'
	# 打印结果：[('123@163.com', ''), ('QAZwsx1@_123.net', '')]

	email_group = re.findall(str,email_addr)
	print('匹配的所有列表是：',email_group)

	# if re.match(str,email_addr):
	# 	return print('邮箱地址符合要求！')
	# else:
	# 	return print('邮箱地址不符合要求，请重新填写!')

while True:
	match_email()
'''
# 输入举例：
# 12345ASDqaz@1wAq.QAZwsx1992-_
# 123 123@163.com asd qwe !24@ QAZwsx1@_123.net

# 2 匹配url
'''
import urlparse
def link_crawler(seed_url, link_regex):
	crawl_queue = [seed_url]
    # keep track which URL's have seen before
	seen = set(crawl_queue)
	while crawl_queue:
		url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html):
            # check if link matches expected regex
            if re.match(link_regex, link):
                # form absolute link
                link = urlparse.urljoin(seed_url, link)
                # check if have already seen this link
                if link not in seen:
                    seen.add(link)
                    crawl_queue.append(link)

def get_links(html):
    """Return a list of links from html
    """
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # list of all links from the webpage
    return webpage_regex.findall(html)
'''
html_string='<img class="course-banner lazy" data-original="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" src="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" style="display: inline;"><img class="course-banner lazy" data-original="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" src="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" style="display: inline;"><img class="course-banner lazy" data-original="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" src="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" style="display: inline;">'

pick=re.findall(r'<img.+?data-original="(.+?)"', html_string)
print (pick)

a = """
<img class="course-banner lazy" data-original="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" src="//img4.hhhaaa.com/5a405d45000175cb06000338-240-135.jpg" style="display: inline;">
"""

p = re.compile ('data-original="(\S+)"')

iterator = p.finditer (a)
for match in iterator:
	print (match.span ())
	print (match.group ())
	print (match.group (1))