import unittest

#2.10
def number_of_words(line):
	return len(line.split())

#2.11
def insert_underscore_everywhere(word):
	return "_".join(list(word))

#2.12
def word_with_first_char(line):
	first_char = [x[0] for x in line.split()]
	return "".join(first_char)

def word_with_last_char(line):
	last_char = [x[-1] for x in line.split()]
	return "".join(last_char)

#2.13
def number_of_char(line):
	return len("".join(line.split()))

#2.14
def the_longest_word(line):
	words = line.split() 
	words.sort(key = len)
	return words[-1]

def number_of_chars_in_the_word(line):
	return len(the_longest_word(line))

#2.15
def sequence_of_consecutive_numbers(L):
	return "".join(str(x) for x in L)

#2.16
def replace_chars(line):
	return line.replace("GvR", "Guido van Rossum")

#2.17
def lexicographical_sorting(line):
	words = line.split()
	words.sort()
	return words

def sorting_by_lenght(line):
	words = line.split()
	words.sort(key = len)
	return words

#2.18
def number_of_digits(number):
	return str(number).count('0')

#2.19
def funny_string(L):
	return ".".join([str(x).zfill(3) for x in L])




class AllTests(unittest.TestCase):
	def test1_number_of_words(self):
		self.assertEqual(number_of_words("Ala\nma\tpieknego kota"), 4)

	def test1_insert_underscore_everywhere(self):
		self.assertEqual(insert_underscore_everywhere("abcdefgh sghij"), "a_b_c_d_e_f_g_h_ _s_g_h_i_j")

	def test1_word_with_first_char(self):
		self.assertEqual(word_with_first_char("Ala\tma kota"), "Amk")

	def test1_word_with_last_char(self):
		self.assertEqual(word_with_last_char("Ala\tma kota"), "aaa")

	def test1_number_of_char(self):
		self.assertEqual(number_of_char("Ala\nma\tpieknego kota"), 17)

	def test1_the_longest_word(self):
		self.assertEqual(the_longest_word("Ala\nma\tpieknego kota"), "pieknego")

	def test1_number_of_chars_in_the_word(self):
		self.assertEqual(number_of_chars_in_the_word("Ala\nma\tpieknego kota"), 8)

	def test1_sequence_of_consecutive_numbers(self):
		self.assertEqual(sequence_of_consecutive_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), "12345678910")

	def test1_replace_chars(self):
		self.assertEqual(replace_chars("This is GvR"), "This is Guido van Rossum")

	def test1_lexicographical_sorting(self):
		self.assertEqual(lexicographical_sorting("Ala\nma\tpieknego kota"), ['Ala', 'kota', 'ma', 'pieknego'])

	def test1_sorting_by_lenght(self):
		self.assertEqual(sorting_by_lenght("Ala\nma\tpieknego kota"), ['ma', 'Ala', 'kota', 'pieknego'])

	def test1_number_of_digits(self):
		self.assertEqual(number_of_digits(102833330000002356000), 10)

	def test1_funny_string(self):
		self.assertEqual(funny_string([1, 346, 14, 38, 2, 456]), "001.346.014.038.002.456" )


if __name__ == "__main__":
  unittest.main()
	

