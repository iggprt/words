

file = open('trouble.txt','r')
content = file.read()

words = content.split()
dict  = {}

for index in range(len(words)):
	current = words.pop(0).lower()
	if current in dict:
		dict[current] += 1
	else:
		dict[current] = 1

max_name = ''
max_num = 0

for index in range(len(dict)):	
	for word in dict:
		if dict[word] > max_num:
			max_name = word
			print dict[word]
	print str(dict[max_name])+ "  ___  "  + max_name
	del dict[max_name]
	max_name = ''
	max_num = 0

while not is_empty(d)
	