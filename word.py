import sqlite3
import re

conn = sqlite3.connect('words.db')
conn.text_factory = str
c = conn.cursor()

def create_tables():
	c.execute("CREATE TABLE IF NOT EXISTS word_tab (word_id integer primary key autoincrement, word, frequency)")
	c.execute("CREATE TABLE IF NOT EXISTS word_found_tab (word_found_id integer primary key autoincrement, word_found, word_id)")
	
def reset_tables():
	create_tables()
	c.execute("drop table word_tab")
	c.execute("drop table word_found_tab")
	create_tables()
	conn.commit()
	
def striped_word(word):
	word = re.sub(r'[\W0-9]','',word)
	return word

def search_word_in_table(word):
	c.execute("select word_id from word_tab where word = :search ;",{'search':word})
	found = c.fetchall()
	if found == []:
		return False
	return found[0][0]

def insert_word(word):
	if search_word_in_table(word):
		c.execute("select frequency from word_tab where word = :w",{'w':word})
		freq = int(c.fetchall()[0][0])
		c.execute("""update word_tab 
					set frequency = :f
					where word_id = :id""",{
					'f':freq+1,
					'id':search_word_in_table(word)})
		conn.commit()
	else:
		c.execute("insert into word_tab (word, frequency) values(:w, 1)",{'w':word})
		conn.commit()
		
		
		 
	


"""	
file = open('troubles.txt','r')
for line in file:
	word_list = line.split()
	for word in word_list:
		if search_word_in_table(word):
			pass
"""		
update_freq('castroane')

"""	

content = file.read()

words = content.split()
dict  = {}
create_tables()
for index in range(len(words)):
	current = words.pop(0).lower()
	current = re.sub(r'\W','',current)
	current = re.sub(r'[0-9]','',current)
	if current == '':
		continue
		
	if current in dict:
		dict[current] += 1
	else:
		dict[current] = 1

for word in sorted(dict, key=dict.__getitem__, reverse = True):
	if dict[word] > 1000:
		print word + " "  +str(dict[word])



for word in dict:
	c.execute('INSERT INTO word_tab(word,frequency) VALUES(:word, :freq)',{
	'word':word,
	'freq':dict[word]})
	
c.execute('select word, word_id from word_tab where word_id = 1')
w = c.fetchall()
print w	

conn.commit()
conn.close()
		
print len(dict)

print re.compile(r'\d').search('12.3') 

"""
