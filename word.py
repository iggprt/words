import sqlite3
import re

conn = sqlite3.connect('words.db')
conn.text_factory = str
c = conn.cursor()

def create_tables():
	c.execute("CREATE TABLE IF NOT EXISTS word_tab (word_id integer primary key autoincrement, word, frequency)")
	c.execute("CREATE TABLE IF NOT EXISTS word_found_tab (word_found_id integer primary key autoincrement, word_found, word_id)")

file = open('trouble.txt','r')
content = file.read()

words = content.split()
dict  = {}

for index in range(len(words)):
	current = words.pop(0).lower()
	current = re.sub(r'\W','',current)
	
	if current in dict:
		dict[current] += 1
	else:
		dict[current] = 1

for word in sorted(dict, key=dict.__getitem__, reverse = True):
	if dict[word] > 20:
		print word + " "  +str(dict[word])
create_tables()
for word in dict:
	c.execute('INSERT INTO word_tab(word,frequency) VALUES(:word, :freq)',{
	'word':word,
	'freq':dict[word]})
conn.commit()
conn.close()
		
print len(dict)
