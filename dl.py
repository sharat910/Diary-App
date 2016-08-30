import sys
import os
from datetime import datetime

#FUNCIONS

def file_open(filename):
	if os.path.isfile(filename):
		f = open(filename,"a")
		f.write("\n\n")
	else:
		f = open(filename,"w")
	return f

def get_filename():
	date = "%s-%s-%s" % (i.day, i.month, i.year)
	filename = date + ".txt"
	return filename

def get_and_write(f):
	i = datetime.now()
	string = "Entry at: " + i.strftime('%Y/%m/%d %H:%M:%S')
	print string

	f.write(string + "\n\n")
	lines = [line for line in sys.stdin]
	f.write("".join(lines))
	f.close()

if __name__ == '__main__':	
	filename = get_filename()
	f = file_open(filename)
	get_and_write(f)
	