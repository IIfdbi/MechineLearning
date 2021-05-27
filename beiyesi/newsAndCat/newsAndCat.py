import pandas as pd
import jieba
import re,numpy

#将原始数据转为DataFame对象
def def_content():
	def_news = pd.read_table('val.txt',names = ['category','theme','URL','content'],encoding = 'utf-8')
	#把空的都删除
	def_news = def_news.dropna()
	# print(def_news.head().content.values)
	#print(def_news.shape)
	#分词，使用结吧分词器
	content = def_news.content.values.tolist()
	# print(content[100])
	#将数据转为DataFrame对象
	content_S = []
	for line in content:
		current_segment = jieba.lcut(line)
		if len(current_segment) > 1 and current_segment != '\r\n':	#换行符
			content_S.append(current_segment)
	# print(content_S[100])
	def_content = pd.DataFrame({'content_S':content_S})
	return def_content

#加载停用词文件，用以清洗数据
def stopwords():
	stopwords = pd.read_csv("./stopwords.txt",index_col = False,sep = "\t",quoting = 3,names = ["stopwords"],encoding = "utf-8")
	# print(stopwords.head())
	return stopwords

#清洗文件
def drop_stopwords(contents,stopwords):
	contents_clean = []
	all_words = []
	for line in contents:
		line_clean = []
		for word in line:
			if word in stopwords:
				continue
			line_clean.append(word)
			all_words.append(str(word))
		contents_clean.append(line_clean)
	# print(all_words[:10])
	return contents_clean,all_words

#查看每个词出现的频率
def viewFrequency(def_all_words):
	words_count = def_all_words.groupby(by=['all_words'])['all_words'].agg({"count":numpy.size})
	words_count = words_count.reset_index().sort_values(by = ["count"],ascending = False)
	return words_count


if __name__ == '__main__':
	def_content = def_content()
	stopwords = stopwords()

	contents = def_content.content_S.values.tolist()
	stopwords = stopwords.stopwords.values.tolist()
	contents_clean,all_words = drop_stopwords(contents,stopwords)
	#将def_content转为DataFrame对象
	def_content = pd.DataFrame({'contents_clean':contents_clean})
	print(def_content.head())

	def_all_words = pd.DataFrame({'all_words':all_words})
	words_count = viewFrequency(def_all_words)

	print(words_count.head())