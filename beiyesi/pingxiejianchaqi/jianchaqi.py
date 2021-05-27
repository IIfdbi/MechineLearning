import re,collections

#返回的是text中包含的所有英文字母，剔除掉了特殊字符例如,._=这些
def words(text):
	return re.findall('[a-z]+',text.lower())

def train(features):
	#将collections里面的属性都设置成默认为1的值
	model = collections.defaultdict(lambda:1)
	#当f在features中的时候，默认model[f]的值会加1
	for f in features:
		model[f] += 1
	return model

if __name__ == '__main__':
	NWORDS = train(words(open('data.txt').read()))

	print(NWORDS)