#import os.path

file_name = raw_input('please select a new filename or an existing one:')

check_flash_file = open(file_name,'a')
print 'initial open and write'
check_flash_file.close()
print 'initial close'
check_flash_file = open(file_name)
print 'open for READ'

if  '{' in check_flash_file.read():
	flashcard = dict(check_flash_file.read())
	print "The file exists!"
else:
	flashcard = {}
	print "The file doesn't exist!"

check_flash_file.close()

ivd = {v: k for k, v in flashcard.items()}
x = 0


while x != 'stop':
	print 'type \'stop\' to stop adding words to the dictionary'

	x = raw_input('keyword:')

	if x == 'stop':
		break
	else:

		y = raw_input('definition:')


	#update dictionary		
	flashcard [x] = y
	ivd = {v: k for k, v in flashcard.items()}

	#remove 'stop' from the dict
	flashcard.pop('stop',0)
	ivd.pop('stop',0)



	print flashcard
	print ivd

flashcard_file = open(file_name,'w')

dict_string = str(flashcard)

flashcard_file.write(dict_string)
flashcard_file.close()


