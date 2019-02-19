
#!/usr/bin/python3
import requests

#网页解析库
from bs4 import BeautifulSoup

#数据结构库
import json

#二位数据结构库
import pandas
import numpy

#数据库操作
import pymysql

# 数据库链接
def mysql():
	conn = pymysql.connect(
	    host='localhost',
	    port=3306,
	    user='root',
	    passwd='',
	    db='test',
	    charset='utf8'
	)
	return conn;

#网页解析 格式化
def htmlFormat(html):
	arrData = [];
	tmpData = [];

	soup = BeautifulSoup(html,"html.parser")
	news = soup.select('#newslist_a .top_newslist .news_top li a')

	# print(news[0].get('href'))

	for name in news:
		tmpData=[name.text,name.get('href')];
		arrData.append(tmpData)

	return arrData;

# 接口数据 格式化
def dataFormat(data):
	tmpStr="";
	tmpData=[];
	arrData=[];
	for name in data:
		tmpData.append(name['params'])

	for i in tmpData:
		if "txt" in i:
			tmpStr=[i['txt'],i['link'],i['imp_url']];
			arrData.append(tmpStr)

	return arrData;

# 数据库添加
def sqlInsert(data):
	conn = mysql();
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor);
	try:
    	# 执行SQL语句，插入数据到 test 表，栏位名称为 title,link,imp_url
		for name in data:
			param=[];
			param=(name[0],name[1],name[2])
			# print(param)
			cursor.execute('insert into leju (title,link,imp_url) values(%s,%s,%s)',param)
	except:
	    print("存入数据库失败")
	# 向数据库提交执行的语句
	conn.commit()
	# 关闭游标
	cursor.close()
	#关闭连接
	conn.close()

# 数据库更新（未完	）
def sqlUpdare(data):
	conn = mysql();
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor);
	try:
    	# 执行SQL语句，插入数据到 test 表，栏位名称为 title,link,imp_url
		# print(data)
		for name in data:
			param=[];
			param=(name[0],name[1],name[2])
			cursor.execute('insert into leju (title,link,imp_url) values(%s,%s,%s)',param)
	except:
	    print("存入数据库失败")
	# 向数据库提交执行的语句
	conn.commit()
	# 关闭游标
	cursor.close()
	#关闭连接
	conn.close()

# 保存excel格式文件
def saveExcel(name,data,columns):
	# 存入excel
	df = pandas.DataFrame(data, columns=columns)

	# 存入多张表
	# writer = pandas.ExcelWriter('test.xlsx')
	# df.to_excel(excel_writer=writer,sheet_name='leju1',mode='a')
	# df.to_excel(excel_writer=writer, sheet_name='leju2')
	# writer.save()
	# writer.close()

	# 存入一个表
	df.to_excel(name+'.xlsx', sheet_name='leju')
	df.to_csv(name+'.csv', mode='a',header=False)# mode 默认 w覆盖写入，a为追加;header为是否写入title

# 循环获取数据
# for num in range(0,2):
# 	res = requests.get('https://www.sina.com.cn/')
# 	res.encoding = 'utf-8'
# 	# 存入数据
# 	data=htmlFormat(res.text);
# 	saveExcel('html',data,['title','link']);

# 接口形式数据
# res = requests.get('https://adm.leju.com/get_abp_list/PG_514AC419D66F33?callback=')

# 获取接口数据
# params = json.loads(res.text)
# 格式化接口数据
# data=dataFormat(params['data']);

# 存入数据
# sqlInsert(data); # 注意列字段个数
# sqlUpdare(data)
# saveExcel('test',data,['title','link','imp_url']);

# 网页形式数据
# res = requests.get('https://www.sina.com.cn/')
# res.encoding = 'utf-8'

# 格式化网页数据
# data=htmlFormat(res.text);
# 存入数据
# saveExcel('html',data,['title','link']);














