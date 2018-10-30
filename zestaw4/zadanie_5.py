#4.5
import unittest

def odwracanie_req(L, left, right):
    if(left < right):
        L[left], L[right] = L[right], L[left]
        odwracanie_req(L, left+1, right-1)
    return L
    
def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left+=1
        right-=1
    return L


class AllTests(unittest.TestCase):
    def test1_owdracanie_req(self):
        self.assertEqual(odwracanie_req([1, 2, 3, 4], 0, 3), [4, 3, 2, 1])
    def test2_owdracanie_req(self):
        self.assertEqual(odwracanie_req([1, 2, 3, 4], 1, 3), [1, 4, 3, 2])
    def test3_owdracanie_iter(self):
        self.assertEqual(odwracanie_req([1, 2, 3, 4], 0, 3), [4, 3, 2, 1])
    def test4_owdracanie_iter(self):
        self.assertEqual(odwracanie_req([1, 2, 3, 4], 1, 3), [1, 4, 3, 2])


if __name__ == "__main__":
  unittest.main()
