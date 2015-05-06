class OutOfRangeError(ValueError):
    pass

class NotIntegerError(ValueError): 
	pass

def toHexa(n):

	if n<0:
		raise OutOfRangeError("OUT OF RANGE")

	if not isinstance(n,int):
		raise NotIntegerError("Non INTEGER CANNOT BE CONVERTED")


	map = ('0','1','2','3','4','5','6','7','8','9',
           'A','B','C','D','E','F')
	s = ''
	while(n/16):
		s += map[n%16]
		n = n/16
	s += map[n%16]
	return s[::-1]




	
	

	

	

	