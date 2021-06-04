from sklearn import tree
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
import pandas as pd
import numpy as np

"""
函数说明：读取txt文件数据
param：
	data - 数据集
return:
	lenses_pd - 返回pd类型的数据(特征值)
	lenses_target - 返回的是最终结果值
"""
def transferFormat(data):
	lenses = [inst.strip().split('\t') for inst in data.readlines()]	#按行份数组再按照Tab键分数据
	# print(lenses)
	lenses_target = []
	for each in lenses:
		lenses_target.append(each[-1])

	lensesLabels = ['age','prescript','astigmatic','tearRate']	#特征属性名
	lenses_dict = {}	#生成字典
	for each_label in lensesLabels:
		lenses_list = []
		for each in lenses:
			lenses_list.append(each[lensesLabels.index(each_label)])	#添加每一个each中位于each_label的值
		lenses_dict[each_label] = lenses_list
	# print(lenses_dict)
	lenses_pd = pd.DataFrame(lenses_dict)	#转为pd格式的数据
	# print(lenses_pd)
	return lenses_pd,lenses_target#!/usr/bin/env python


"""
函数说明：序列化数据
param：
	lenses_pd - pd.DataFrame类型的数据
return:
	lenses_pd - 序列化后的pd.DataFrame类型的数据
"""
def seriesData(lenses_pd):
	le = LabelEncoder()
	for col in lenses_pd.columns:	#为每一行序列化
		lenses_pd[col] = le.fit_transform(lenses_pd[col])	#fit_transform函数的作用是序列话
	return lenses_pd

"""
函数说明：绘制决策树
param：
	lenses_pd - 数据集
	lenses_target - 结果值
return
	绘制好的决策树
"""
def buildDecisionTree(lenses_pd,lenses_target):
	clf = tree.DecisionTreeClassifier(max_depth = 4)	#创建DecisionTreeClassfier类
	clf = clf.fit(lenses_pd.values.tolist(),lenses_target)	#初始化数据，用以构建决策树
	print(clf)
	return None

if __name__ == '__main__':
	fr = open('data.txt')
	lenses_pd,lenses_target = transferFormat(fr)
	# print(lenses_target)
	# print(lenses_pd)
	lenses_pd = seriesData(lenses_pd)
	print(lenses_pd)
	buildDecisionTree(lenses_pd,lenses_target)
