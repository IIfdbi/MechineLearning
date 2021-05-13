import numpy as np
import operator

"""
函数说明：创建数据集
parameters:
	无
return:
	group - 数据集
	labels - 标签

"""
def createDataSet():
	#四组数据，这里的数据可以从文件里面获取
	group = np.array([[1,101],[5,89],[106,5],[110,10]]) 
	#设置标签，标签同上
	labels = ['爱情片','爱情片','动作片','动作片']

	return group , labels

"""
函数说明：创建KNN分类器
parameters:
	test - 用于分类的数据（测试集）
	dataSet - 用于训练的数据（训练集）
	labels - 标签
	k - KNN参数，选取的距离最小的前K个值，一般不超过20
return：
	分类结果
"""
def classfy(test,dataSet,labels,k):
	#返回训练集的长度
	dataSize = dataSet.shape[0]
	#计算欧式距离,np.tile(A,B)重复A这个B次
	diffMat = np.tile(test,(dataSize,1)) - dataSet
	diffMat = diffMat**2
	diffMat = diffMat.sum(axis = 1)
	diffMat = diffMat**0.5
	#返回diffMat 中元素从小到大排序后的索引值
	sortDistIndices = diffMat.argsort()

	#定义一个记录类别次数的字典
	classCount = {}
	for i in range(k):
		#用取出前K个中的索引值来找到对应的类别
		voteLabel = labels[sortDistIndices[i]]
		#计算类别次数,这里面的get方法里面添加参数0 是因为如果这个字典中不包含有这个键值名，那么默认为0
		classCount[voteLabel] = classCount.get(voteLabel,0) + 1
	#operator.itermgetter(1)根据字典中的值进行排序
	#					  0	            键值名
	#reverse降序排序字典
	# sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
	# 上式子也可以这么写
	sortedClassCount = sorted(classCount.items(),key = lambda item:item[1],reverse = True)
	return sortedClassCount

if __name__ == '__main__':
	#训练集
	group,labels = createDataSet()
	#测试集
	test = [100,20]

	#进行KNN分类并返回值
	testClass = classfy(test,group,labels,3)
	print(testClass)
	#这里打印出哪一类就行了
	print(testClass[0][0])


