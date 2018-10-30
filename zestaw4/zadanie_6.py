#4.6
import unittest

def sum_seq(sequence):
    output = 0;
    if isinstance(sequence, (list, tuple)):
        for x in sequence:
            output += int(sum_seq(x))
    else:
        return sequence
    return output


class AllTests(unittest.TestCase):
    def test1_sum_seg(self):
        self.assertEqual(sum_seq([[],[4],(1,2),[3,4],(5,6,7)]), 32)


if __name__ == "__main__":
  unittest.main()
