from math import log
import operator
"""
函数说明：创建测试数集
Returns:
	dataSet - 数据集
	labels - 分类属性
"""
def createDataSet():
	dataSet = [[0, 0, 0, 0, 'no'], #数据集
			[0, 0, 0, 1, 'no'],
			[0, 1, 0, 1, 'yes'],
			[0, 1, 1, 0, 'yes'],
			[0, 0, 0, 0, 'no'],
			[1, 0, 0, 0, 'no'],
			[1, 0, 0, 1, 'no'],
			[1, 1, 1, 1, 'yes'],
			[1, 0, 1, 2, 'yes'],
			[1, 0, 1, 2, 'yes'],
			[2, 0, 1, 2, 'yes'],
			[2, 0, 1, 1, 'yes'],
			[2, 1, 0, 1, 'yes'],
			[2, 1, 0, 2, 'yes'],
			[2, 0, 0, 0, 'no']]
	labels = ['年龄', '有工作','有自己的房子','信贷情况'] #特征标签
	return dataSet,labels
"""
函数说明：计算给定数据集的熵
param：
	dataSet - 数据集
return:
	entropy - 熵值
"""	
def calculateEntropy(dataSet):
	numOfData = len(dataSet)
	labelCount = {}
	for data in dataSet:
		currentLabel = data[-1]
		if currentLabel not in labelCount.keys():
			labelCount[currentLabel] = 0
		labelCount[currentLabel] += 1
	entropy = 0.0
	for key in labelCount:
		prob = float(labelCount[key]) / numOfData #计算每一个label出现的概率
		entropy -= prob * log(prob,2)
	return entropy
"""
函数说明：信息增益计算并选择最优特征
param：
	dataSet - 数据集
return:
	bestFeature - 信息增益最大的特征的索引值
"""
def chooseBestImformationGain(dataSet):
	featureNum = len(dataSet[0][0:-1])	#找到有多少个数据特征
	baseEntropy = calculateEntropy(dataSet)	#得到熵值
	bestImforGain = 0.0 #先设置好最好的信息增益的哨兵
	bestImforGainLoc = -1	#先设置好最好的信息增益的特征的位置
	for i in range(featureNum):
		featList = [data[i] for data in dataSet]
		uniqueVals = set(featList)	#创建set集合{},元素不可重复
		newEntropy = 0.0
		for value in uniqueVals:
			#得到按照不同特征划分好的集合subDataSet
			subDataSet = splitDataSet(dataSet,i,value)
			#算一下这个subDataSet在总共的数据集中占比多少
			prob = len(subDataSet) / float(len(dataSet))
			#用subDataSet做熵值运算
			currentEntropy = calculateEntropy(subDataSet)
			newEntropy += prob * currentEntropy
		print("%.3f ----- %.3f" % (baseEntropy,newEntropy))
		informationGain = baseEntropy - newEntropy
		print("第%d个特征的增益为 %.3f" % (i,informationGain))
		if informationGain > bestImforGain :
			bestImforGain = informationGain
			bestImforGainLoc = i
	print("最好的信息增益值为：%.3f，是第%d个特征" % (bestImforGain,bestImforGainLoc))	
	return bestImforGain,bestImforGainLoc
			
""" 
函数说明：根据列号划分好不同的特征的数据
param：
	dataSet - 数据集
return：
	dataSet - 按照不同特征分好类的数据集
	no - 不批准贷款
	yes - 批准贷款
"""
def splitDataSet(dataSet,i,value):
	subDataSet = []

	for featureVec in dataSet:
		if featureVec[i] == value:
			reduceFeatVec = featureVec[:i]	#执行实现删除i列与value值相等的数据，返回其他列的数据
			reduceFeatVec.extend(featureVec[i+1:])
			subDataSet.append(reduceFeatVec)
			
	return subDataSet  
			

"""
函数说明：创建决策树
param:
	dataSet - 数据集
	labels - 分类属性标签
	featLabels - 存储选择的最优特征标签
Returns:
	myTree - 决策树
"""
def createTree(dataSet,labels):
	print(dataSet)
	print(labels)
	print("~~~~~~~")
	classList = [example[-1] for example in dataSet]	#取分类标签（是否放贷：yes / no）
	if classList.count(classList[0]) == len(classList):	#如果类别完全相同的时候则停止继续划分
		return classList[0]	#返回这个标签
	if len(dataSet[0]) == 1 or len(labels) == 0:	#当递归循环到测试集合的长度为1或者是标签特征全部用完之后姐结束构建书了
		return majorityCnt(classList)
	bestImforGain,bestFeat = chooseBestImformationGain(dataSet)	#选择最优特征，找到最优特征的位置
	bestFeatLabel = labels[bestFeat]	#得出最优特征的标签
	# featLabels.append(bestFeatLabel)	#将得出来的最优的标签添加到集合中
	myTree = {bestFeatLabel:{}}	#根据每次的最优标签生成树
	del(labels[bestFeat])	#删除已经使用过的标签
	featValues = [example[bestFeat] for example in dataSet]	#得到训练集中所有的最优特征的属性值
	uniqueVals = set(featValues)	#去掉重复的属性值
	for value in uniqueVals:
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,bestFeat,value),labels)
		
	return myTree

"""
函数说明：统计classList中出现次数最多的元素
param：	
	classList	-	类标签列表
returns:
	sortedClassCount[0][0] - 返回最多出现次数的类标签
"""
def majorityCnt(clasList):
	classCount = {}
	for vote in clasList:
		if vote not in classCount:
			classCount[vote] = 0
		classCount += 1
	sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
	return sortedClassCount[0][0]
				
if __name__ == '__main__':
	dataSet,labels = createDataSet()
	# entropy = calculateEntropy(dataSet)
	# print(entropy)
	# bestImforGain,bestImforGainLoc = chooseBestImformationGain(dataSet)
	# print("最好的信息增益值为：%.3f，是第%d个特征" % (bestImforGain,bestImforGainLoc + 1))
	# featLabels = []
	# myTree = createTree(dataSet,labels,featLabels)
	myTree = createTree(dataSet,labels)
	print(myTree)
	

	
	
	
	
	
	