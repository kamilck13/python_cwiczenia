#12.2
import unittest

def czy_posortowane(L):
    for i in range(1, len(L)):
        if(L[i] < L[i-1]):
            return False
    return True   

def binarne_rek(L, left, right, y):
    if not czy_posortowane(L):
        raise AssertionError("Elementy nie są posortowane (uporządkowane)")
    mid = int((left + right)/2)
    if(L[mid] < y):
        return binarne_rek(L, mid+1, right, y)
    elif(L[mid] > y):
        return binarne_rek(L, left, mid-1, y)
    else:
        return mid
    return None
    

class AllTests(unittest.TestCase):
    def test1(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 6, 5), 4)
    def test2(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 0, 4, 2), 1)
    def test3(self):
        L = (1, 2, 3, 4, 5, 6, 7)
        self.assertEqual(binarne_rek(L, 3, 7, 4), 3)
        

if __name__ == "__main__":
    unittest.main()
