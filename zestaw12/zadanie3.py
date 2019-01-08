#12.3
import unittest

def mediana_sort(L, left, right):
    sort = sorted(L)
    length = right - left
    mid = int(left + right/2)
    if not length % 2:
       return sort[mid] #wybieram element środkowy
    else:
       return sort[int(length/2)] #przyjmuję medianę dolną
 
   
class AllTests(unittest.TestCase):
    def test1(self):
        L = [5, 2, 4, 3, 1]
        self.assertEqual(mediana_sort(L, 0, 4), 3)
    def test2(self):
        L = [5, 8, -1, 6, 6, 1, 10]
        self.assertEqual(mediana_sort(L, 0, 6), 6)
    def test3(self):
        L = [6, 8, 3, 4, 9, 2]
        self.assertEqual(mediana_sort(L, 0, 5), 4)


if __name__ == "__main__":
    unittest.main()
