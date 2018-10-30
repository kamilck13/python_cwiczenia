#4.4
import unittest

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a+b
	return a


class AllTests(unittest.TestCase):
	def test1_fib(self):
		self.assertEqual(fib(0), 0)

	def test2_fib(self):
		self.assertEqual(fib(6), 8)
		
if __name__ == "__main__":
  unittest.main()

