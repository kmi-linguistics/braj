import csv
import os
import re

#cur_dir = os.getcwd()
cur_dir = 'edited-corpus'

with open ('test_file.conll', 'w') as f_write:
	for cur_file in os.listdir(cur_dir):
		if cur_file.endswith('.txt'):
			f_p = os.path.join (cur_dir, cur_file)
			with open (f_p) as f:
				data = f.read().strip().replace('\n\n', '\n').replace('\n', ' ').replace('  ', ' ')
				sents = re.split(r'([\u0964!?])', data)
				print (sents)
				for i in range (0, len(sents), 2):
					sent = sents[i].strip()
					if sent != '':
						words = sent.split()
						if i < len(sents) - 1:
							punct = sents[i+1]
						else:
							punct = ''
						for word in words:
							f_write.write (word + '\n')
						if punct != '':
							f_write.write (punct + '\n\n')