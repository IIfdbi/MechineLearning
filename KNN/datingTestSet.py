import numpy as np
from matplotlib.font_manager import FontProperties
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

"""
函数说明：打开文件且对数据分类，1是代表不喜欢，2是代表魅力一般，3是代表极具魅力
parameters:
	filename - 文件名
returns:
	returnMat - 特征矩阵
	classLabelVector - 分类Label向量
"""
def file2Matrix(filename):
	fn = open(filename)
	#读取文件中的所有内容
	arrayLines = fn.readlines()
	#获取文件行数
	lenArrayLines = len(arrayLines)
	#建造一个numpy矩阵
	returnMat = np.zeros((lenArrayLines,3))
	#返回分类标签向量
	classLabelVector = []
	index = 0
	for line in arrayLines:
		#切片并获取数据
		line = line.strip()
		listFromLine = line.split('\t')
		#将数据前三列提取出来，逐个存放在returnMat中，returnMat[index,:],根据index值然后更新returnMat中的所有行的值
		
		returnMat[index,:] = listFromLine[0:3]
		#将喜欢程度转换为数字，1是代表不喜欢，2是代表魅力一般，3是代表极具魅力
		if listFromLine[-1] == 'didntLike':
			classLabelVector.append(1)
		elif listFromLine[-1] == 'smallDoses':
			classLabelVector.append(2)
		elif listFromLine[-1] == 'largeDoses':
			classLabelVector.append(3)
		index += 1		
	return returnMat,classLabelVector


"""
函数说明:可视化数据
 
Parameters:
    datingDataMat - 特征矩阵
    datingLabels - 分类Label
Returns:
    无
Modify:
    2017-03-24
"""
def showdatas(datingDataMat, datingLabels):
    #设置汉字格式
    font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
    #将fig画布分隔成1行1列,不共享x轴和y轴,fig画布的大小为(13,8)
    #当nrow=2,nclos=2时,代表fig画布被分为四个区域,axs[0][0]表示第一行第一个区域
    fig, axs = plt.subplots(nrows=2, ncols=2,sharex=False, sharey=False, figsize=(13,8))
 
    numberOfLabels = len(datingLabels)
    LabelsColors = []
    for i in datingLabels:
        if i == 1:
            LabelsColors.append('black')
        if i == 2:
            LabelsColors.append('orange')
        if i == 3:
            LabelsColors.append('red')
    #画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第二列(玩游戏)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][0].scatter(x=datingDataMat[:,0], y=datingDataMat[:,1], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs0_title_text = axs[0][0].set_title(u'每年获得的飞行常客里程数与玩视频游戏所消耗时间占比',FontProperties=font)
    axs0_xlabel_text = axs[0][0].set_xlabel(u'每年获得的飞行常客里程数',FontProperties=font)
    axs0_ylabel_text = axs[0][0].set_ylabel(u'玩视频游戏所消耗时间占',FontProperties=font)
    plt.setp(axs0_title_text, size=9, weight='bold', color='red') 
    plt.setp(axs0_xlabel_text, size=7, weight='bold', color='black') 
    plt.setp(axs0_ylabel_text, size=7, weight='bold', color='black')
 
    #画出散点图,以datingDataMat矩阵的第一(飞行常客例程)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[0][1].scatter(x=datingDataMat[:,0], y=datingDataMat[:,2], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs1_title_text = axs[0][1].set_title(u'每年获得的飞行常客里程数与每周消费的冰激淋公升数',FontProperties=font)
    axs1_xlabel_text = axs[0][1].set_xlabel(u'每年获得的飞行常客里程数',FontProperties=font)
    axs1_ylabel_text = axs[0][1].set_ylabel(u'每周消费的冰激淋公升数',FontProperties=font)
    plt.setp(axs1_title_text, size=9, weight='bold', color='red') 
    plt.setp(axs1_xlabel_text, size=7, weight='bold', color='black') 
    plt.setp(axs1_ylabel_text, size=7, weight='bold', color='black')
 
    #画出散点图,以datingDataMat矩阵的第二(玩游戏)、第三列(冰激凌)数据画散点数据,散点大小为15,透明度为0.5
    axs[1][0].scatter(x=datingDataMat[:,1], y=datingDataMat[:,2], color=LabelsColors,s=15, alpha=.5)
    #设置标题,x轴label,y轴label
    axs2_title_text = axs[1][0].set_title(u'玩视频游戏所消耗时间占比与每周消费的冰激淋公升数',FontProperties=font)
    axs2_xlabel_text = axs[1][0].set_xlabel(u'玩视频游戏所消耗时间占比',FontProperties=font)
    axs2_ylabel_text = axs[1][0].set_ylabel(u'每周消费的冰激淋公升数',FontProperties=font)
    plt.setp(axs2_title_text, size=9, weight='bold', color='red') 
    plt.setp(axs2_xlabel_text, size=7, weight='bold', color='black') 
    plt.setp(axs2_ylabel_text, size=7, weight='bold', color='black')

    #自己画一个散点图
    axs[1][1].scatter(x = datingDataMat[:,0],y = datingDataMat[:,2],color = LabelsColors,s = 15,alpha = 0.5)
    # axs3_title_text = axs[1][1].set_title(u'demo',FontProperties = font)
    # axs3_xlabel_text = axs[1][1].set_xlabel(u'x轴')
    # axs3_ylabel_text = axs[1][1].set_ylabel(u'y轴')



    #设置图例
    didntLike = mlines.Line2D([], [], color='black', marker='.',
                      markersize=6, label='didntLike')
    smallDoses = mlines.Line2D([], [], color='orange', marker='.',
                      markersize=6, label='smallDoses')
    largeDoses = mlines.Line2D([], [], color='red', marker='.',
                      markersize=6, label='largeDoses')
    #添加图例
    axs[0][0].legend(handles=[didntLike,smallDoses,largeDoses])
    axs[0][1].legend(handles=[didntLike,smallDoses,largeDoses])
    axs[1][0].legend(handles=[didntLike,smallDoses,largeDoses])
    #显示图片
    plt.show()

"""
函数说明：对数据进行归一化
parameter:
	dataSet - 特征矩阵
returns:
	normDataSet - 归一化后的特征矩阵
"""
def autoNorm(dataSet):
	normDataSet = np.zeros(np.shape(dataSet))
	length = dataSet.shape[0]
	#将三列数据都归一化 
	for i in range(3):
		#取每一列数据遍历
		data = dataSet[:,i]
		#将行转换为列
		# data = data.reshape(length,1)
		#获取到最大最小值
		minVals = data.min()
		maxVals = data.max()
		#获取到每一列数据的取值范围
		ranges = maxVals - minVals
		#计算每一个数值归一化后的值
		normDataSet[:,i] = data - np.tile(minVals,length)
		normDataSet[:,i] = normDataSet[:,i] / ranges

	return normDataSet,ranges,minVals


"""
函数说明: 分类器测试函数
parameters:
	无
returns:
	normDataSet - 归一化后的特征举证
	ranges - 数据范围
	minVals - 数据最小值
"""
def datingClassTest():
	filename = "./datingTestSet.txt"
	datingDataMat, datingLabels = file2Matrix(filename)
	# 数据可视化展示
	# showdatas(datingDataMat, datingLabels)
	hoRatio = 0.1
	normDataSet,ranges,minVals = autoNorm(datingDataMat)
	length = normDataSet.shape[0]
	#用于测试所使用的个数
	testNums = int(hoRatio*length)
	errorCount = 0
	for i in range(testNums):
		#前面testNums作为测试集，normDataSet[testnums:]作为训练集合
		#循环遍历前testNums中的数据
		classfyResult = classfy(normDataSet[i,:],normDataSet[testNums:length,:],datingLabels[testNums:length],4)
		print("分类结果：%5d 真实类别为：%d" % (classfyResult,datingLabels[i]))
		if classfyResult != datingLabels[i]:
			errorCount += 1 
			print("~~~~~~~")

	print("错误率：%f%%" %(errorCount/float(testNums)*100))
	print(errorCount,testNums)
"""
函数说明：KNN分类器
parameters:
	test:测试集
	dataSet:训练集
	labels - 标签
	k - KNN参数，选取的距离最小的前K个值，一般不超过20
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


"""
函数说明：通过输入一个人的三个特征，进行分类输出
parameters:
	无
returns:
	无
"""
def classfyPersonal():
	resultList = ["讨厌","有些喜欢","非常喜欢"]
	precentTats = float(input("玩视频游戏所耗时间百分比:"))
	ffMiles = float(input("每年获得的飞行常客里程数:"))
	iceCream = float(input("每周消费的冰激淋公升数:"))
	#打开的文件名
	filename = "datingTestSet.txt"
	#打开并处理数据
	datingDataMat, datingLabels = file2matrix(filename)
	#训练集归一化
	normMat, ranges, minVals = autoNorm(datingDataMat)
	#生成NumPy数组,测试集
	inArr = np.array([ffMiles, precentTats, iceCream])
	#测试集归一化
	norminArr = (inArr - minVals) / ranges
	#返回分类结果
	classifierResult = classfy(norminArr, normMat, datingLabels, 3)
	#打印结果
	print("你可能%s这个人" % (resultList[classifierResult-1]))

if __name__ == '__main__':
	# filename = "./datingTestSet.txt"
	# datingDataMat, datingLabels = file2Matrix(filename)
	# print(datingDataMat)
	# 数据可视化展示
	# showdatas(datingDataMat, datingLabels)

	#将数据归一化
	# normDataSet,ranges,minVals = autoNorm(datingDataMat)
	# print(normDataSet)
	 
	# 测试KNN算法最后的正确性
	# datingClassTest()

	#输入一个人的信息用KNN算法来判断是不是喜欢的人
	classfyPersonal()