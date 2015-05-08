import sys

if __name__ == '__main__':

	print 'filename - %s' % sys.argv[0]
	for arg in sys.argv[1:]:
		print 'Argument - %s' %arg
