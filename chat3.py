
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')        #清單用空白鍵分割
	time = s[0][:5]            #s[0]中0-4個字
	name = s[0][5:]            #s[0]中5-最後個字
	print(name)

	print
