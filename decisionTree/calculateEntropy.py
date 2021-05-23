from math import log
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
	labels = ['不放贷', '放贷'] #分类属性
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
		informationGain = baseEntropy - newEntropy
		print("第%d个特征的增益为 %.3f" % (i,informationGain))
		if informationGain > bestImforGain :
			bestImforGain = informationGain
			bestImforGainLoc = i
		
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
def splitDataSet(dataSeti,i,value):
	subDataSet = []
	no = 0
	yes = 0
	for featureVec in dataSet:
		if featureVec[i] == value:
			subDataSet.append(featureVec)

	return subDataSet  
			
				
if __name__ == '__main__':
	dataSet,features = createDataSet()
	# entropy = calculateEntropy(dataSet)
	# print(entropy)
	bestImforGain,bestImforGainLoc = chooseBestImformationGain(dataSet)
	print("最好的信息增益值为：%.3f，是第%d个特征" % (bestImforGain,bestImforGainLoc + 1))

	
	
	
	
	
	