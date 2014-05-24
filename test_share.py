import unittest
import os
from share import *

invalid_input = 'Invalid file type or format'
path1 = '/'.join([folder_path, 'csv', 'test_data_1.csv']) # sample test data two
output1 = [['company 1', 246, '1991', 'feb'], ['company 2', 245, '1990', 'jan'], ['company 3', 243, '1990', 'jan'], ['company 4', 235, '1991', 'may'], ['company 5', 245, '1991', 'june']]

path2 = '/'.join([folder_path, 'csv', 'test_data_2.doc']) # for invalid file type
output2 = invalid_input

path3 = '/'.join([folder_path, 'csv', 'test_data_3.txt']) # accepting a txt for csv but missing column headers
output3 =  invalid_input

path4 = '/'.join([folder_path, 'csv', 'test_data_4.csv']) # for empty file
output4 =  invalid_input

path5 = '/'.join([folder_path, 'csv', 'data.csv']) # for proper data and output
output5 = [['company 1', 498, 'dec', '1996'], ['company 2', 499, 'jan', '2002'], ['company 3', 499, 'aug', '1995'], ['company 4', 499, 'nov', '2001'], ['company 5', 497, 'jan', '2002']]



class TestSuit(unittest.TestCase):
	def setUp(self):
		self.path1 = path1
		self.path2 = path2
		self.path3 = path3
		self.path4 = path4
		self.path5 = path5

	def test_file_is_empty(self):
		self.assertNotEqual(os.stat(path1).st_size, 0)
		self.assertNotEqual(os.stat(path2).st_size, 0)
		self.assertNotEqual(os.stat(path3).st_size, 0)
		self.assertEqual(os.stat(path4).st_size, 0)
		self.assertNotEqual(os.stat(path5).st_size, 0)


	def checkfileformat(self, path, test_flag):
		with open(path, 'r') as file_obj:
			flag = check_file_format(file_obj)
			self.assertEqual(flag, test_flag)

	def test_fileformat(self):
		self.checkfileformat(path1, True)
		self.checkfileformat(path2, False)
		self.checkfileformat(path3, False)
		self.checkfileformat(path4, False)
		self.checkfileformat(path5, True)


	def each_fileread(self, path, expected_output, expect=True):
		if expect:
			output = [list(l) for l in get_list(path)]
			self.assertEqual(output, expected_output)
		else:
			self.assertEqual(invalid_input, expected_output)
		
	def test_output(self):
		self.each_fileread(path1, output1, expect=True)
		self.each_fileread(path2, output2, expect=False)
		self.each_fileread(path3, output3, expect=False)
		self.each_fileread(path4, output4, expect=False)
		self.each_fileread(path5, output5, expect=True)

if __name__ == '__main__':
    unittest.main()