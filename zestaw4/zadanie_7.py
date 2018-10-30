#4.7
import unittest

def flatten(sequence):
    output = list()
    if isinstance(sequence, (list, tuple)):
        for x in sequence:
            if isinstance(x, (list, tuple)):
                tmp = flatten(x)
                output += tmp
            else:
                output.append(x)
    return output


class AllTests(unittest.TestCase):
    def test1_flatten(self):
        self.assertEqual(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]), [1,2,3,4,5,6,7,8,9])


if __name__ == "__main__":
  unittest.main()
