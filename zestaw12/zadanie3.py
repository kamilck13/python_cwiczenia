#12.3
import unittest

def mediana_sort(L, left, right):
    sort = sorted(L)
    length = right - left + 1
    mid = int(length / 2) + left
    if length == 1:
        return sort[left]
    if not length % 2:
        x = sort[mid]
        y = sort[mid-1]
        return (x + y) / 2
    else:
        return sort[mid]


class AllTests(unittest.TestCase):
    def test1(self):
        L = [5, 2, 4, 3, 1, 6]
        self.assertEqual(mediana_sort(L, 2, 5), 4.5)
    def test11(self):
        L = [5, 2, 4, 3, 1, 6]
        self.assertEqual(mediana_sort(L, 2, 2), 3)
    def test12(self):
        L = [5, 2, 4, 3, 1, 6]
        self.assertEqual(mediana_sort(L, 2, 3), 3.5)
    def test13(self):
        L = [5, 2, 4, 3, 1, 6]
        self.assertEqual(mediana_sort(L, 2, 4), 4)
    def test14(self):
        L = [5, 2, 4, 3, 1, 6]
        self.assertEqual(mediana_sort(L, 1, 4), 3.5)

    def test2(self):
        L = [5, 8, -1, 6, 6, 1, 10]
        self.assertEqual(mediana_sort(L, 0, 6), 6)

    def test3(self):
        L = [6, 8, 3, 4, 9, 2]
        self.assertEqual(mediana_sort(L, 0, 5), 5)

    def test4(self):
        L = [2]
        self.assertEqual(mediana_sort(L, 0, 0), 2)

    def test5(self):
        L = [6, 8]
        self.assertEqual(mediana_sort(L, 0, 1), 7)


if __name__ == "__main__":
    unittest.main()
