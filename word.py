

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

for word in sorted(dict, key=dict.__getitem__, reverse = True):
	if dict[word] > 30:
		print word + " "  +str(dict[word])