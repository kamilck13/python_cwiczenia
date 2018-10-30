#4.3
import unittest

def factorial(n):
	tmp = 1
	if n in (0,1):
		return 1
	else:
		for i in range(2, n+1):
			tmp = tmp * i
		return tmp
	
class AllTests(unittest.TestCase):
	def test1_factorial(self):
		self.assertEqual(factorial(3), 6)
	def test2_factorial(self):
		self.assertEqual(factorial(0), 1)
	def test3_factorial(self):
		self.assertEqual(factorial(6), 720)

if __name__ == "__main__":
  unittest.main()
