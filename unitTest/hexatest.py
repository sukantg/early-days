import hexa
import unittest

class samples(unittest.TestCase):

	pairs = (
		(1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'),
        (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'A'),
        (11,'B'), (12,'C'), (13,'D'), (14,'E'), (15,'F'),
        (16,'10'), (30,'1E'), (127,'7F'), (255,'FF'), (500,'1F4'),
        (1024,'400'), (5100,'13EC'), (65535,'FFFF'), (65536,'10000')

	)

	def testHexa(self):
		for des,he in self.pairs:
			result = hexa.toHexa(des)
			self.assertEqual(des,result)

class badSamples(unittest.TestCase):
	''' toHex should fail when the input < 0'''
	def testNegativeHexa(self):
		self.assertRaises(hexa.OutOfRangeError,hexa.toHexa,-1)
	'''to_roman should fail with non-integer input'''
	def testNonInteger(self):
		self.assertRaises(hexa.NotIntegerError,hexa.toHexa,0.5)


if __name__ == '__main__':
    unittest.main()