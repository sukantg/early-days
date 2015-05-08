import getopt, sys

def main():
	in_filename = 'fin'
	out_filename = 'fout'

	print 'Arguments - %s' % sys.argv[1:]

	try:
		options,remainder = getopt.getopt(sys.argv[1:],'i:o',['input=','output='])
	except getopt.GetoptError:
		sys.exit()


	print 'Options - %s' % (options)

	for opt, arg in options:
		if opt in ('-i','--input'):
			in_filename = arg
		if opt in ('-o','--output'):
			out_filename = arg

	print 'Remainder - %s' % (remainder)
	print 'Input Argument - %s' % (in_filename)
	print 'Output Argument - %s' % (out_filename)




if __name__ == '__main__':
	sys.exit(main())

