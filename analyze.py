# coding: utf-8

# ### 数据处理部分


import pandas as pd
data=pd.read_excel('房数据.xlsx')#导入数据



ca=data['信息'].str.split('|',expand=True)#对信息列进行分列得到想要的数据

dat=ca.iloc[:,0:5]
dat.rename(columns={0:'房型',1:'面积',2:'层数',3:'朝向',4:'年份'},inplace=True)#将信息列分开再重新组合

data1=pd.concat([data['标题'],dat,data['价格']],axis=1)#合并最后的表格

data1.info()#去除空值

data1.drop_duplicates(inplace=True)#去除重复值


home={'2室2厅':'中户型','3室2厅':'中户型','2室1厅':'小户型',
      '1室1厅':'小户型','3室1厅':'小户型','4室2厅':'中户型',
      '独栋':'大户型','1室0厅':'小户型','5室2厅':'中户型',
      '3室3厅':'大户型','4室3厅':'大户型','4室1厅':'小户型',
      '1室2厅':'中户型','联排':'大户型','5室3厅':'大户型',
      '6室4厅':'大户型','5室6厅':'大户型','5室5厅':'大户型',
      '5室4厅':'大户型','6室2厅':'大户型','4室4厅':'大户型',
      '6室3厅':'大户型','3室4厅':'大户型','5室1厅':'大户型','叠加':'大户型'}#构建对应字典

data1['房型']=data1['房型'].map(home)#对房型的划分

##对面积的处理
data1.index=list(range(len(data1['面积'])))#重置索引，因为前面去除重复值导致索引混乱
for i in range(len(data1['面积'])):
    data1['面积'][i]=data1['面积'][i][:-1]


data1['面积'][data1['面积'].str.contains('卧室')]=None#去除杂音




#对层数的处理
for i in range(len(data1['层数'])):
    data1['层数'][i]=data1['层数'][i][0:2]




#对年份的处理，去除‘年建’这两个字
for i in range(len(data1['年份'])):
    data1['年份'][i]=data1['年份'][i][0:4]



data1['年份'].value_counts()



data1.info()#查看数据类型，将面积，价格改为数值类类型



data1.dropna(inplace=True)#最后去除空值



data1['价格']=data1['价格'].astype('float')#转换数据格式



data1['面积']=data1['面积'].astype('float')


data1.info()


data1.to_excel('房数据分析后.xlsx')

# ### 可视化部分


import matplotlib.pyplot as plt#画图的库
import seaborn as sns#画图的库
sns.set(style="darkgrid")#设置画图风格


import numpy as np#数据处理库
plt.figure(figsize=(10,8))
plt.rcParams['font.sans-serif']=['SimHei']#设置显示中文
plt.rcParams['axes.unicode_minus'] = False#设置显示中文
plt.hist(np.log(data1['价格']),bins=50)#对数化处理价格,使其正态分布
plt.show()


#解决中文显示问题
plt.figure(figsize=(10,8))
sns.boxplot(data1['房型'],np.log(data1['价格']))#画图，将价格对数化处理，图更好看
plt.show()#展示图


plt.figure(figsize=(10,8))#设置画布
plt.scatter(data1['面积'],data1['价格'])#面积价格图
plt.show()


plt.figure(figsize=(10,8))
sns.boxplot(data1['层数'],np.log(data1['价格']))#对数化处理价格
plt.show()


plt.figure(figsize=(10,8))
sns.boxplot(data1['朝向'],np.log(data1['价格']))#对数化处理价格
plt.show()