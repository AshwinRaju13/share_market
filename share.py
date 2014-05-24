import os
import sys

import csv

sys.dont_write_bytecode = True
delimiter = ','

folder_path = os.path.dirname(os.path.realpath(__file__))
PATH = '/'.join([folder_path, 'csv', 'data.csv'])
ALLOWED_TYPES = ['csv', 'txt']

def get_max_share_price(col):
	'''
		Method to return the max share for a company
	'''
	col = list(col)
	max_share = reduce(max, map(int, col[1:]))
	return (max_share, col.index(str(max_share)))


def get_column(filename, col=0):
	'''
		Generator method which return a column from csv
	'''
	for row in csv.reader(open(filename), delimiter=delimiter):
		yield row[col]


def get_list(PATH):
	'''
		Returing a generator of list of company, share, year and month.
	'''
	with open(PATH, 'r') as file_obj:
		first_row = file_obj.readline().split(delimiter)
		num_cols = len(first_row) 
		year = []
		month = []
		for i in xrange(num_cols): # to start from Company column
			col = get_column(PATH, i)
			if i == 0:
				year = list(col)
			elif i == 1:
				month = list(col)
			else:
				company = first_row[i].strip()
				share, index =  get_max_share_price(col)
				yield company, share, year[index], month[index]


def file_is_empty(path):
	'''
		Check if file is file_is_empty
	'''
	return os.stat(path).st_size==0


def check_file_format(file_obj):
	'''
		Method returninf true or false based on validating file format.
	'''
	first_row = file_obj.readline().split(delimiter)
	if 'year' in first_row and 'month' in first_row:
		flag = (first_row.index('year') == 0) and (first_row.index('month')==1)
		for each in first_row[2:]:
			if each.strip().lower().startswith('company'):
				flag = flag and True
			else:
				flag = flag and False
	else:
		flag = False
	return flag


def file_is_valid(file_obj, PATH):
	'''
	Method returning True or False based on validity of the input file
	'''
	flag = True
	flag = not file_is_empty(PATH) and flag
	flag = flag and (PATH.endswith('.txt') or PATH.endswith('.csv'))
	flag = flag and check_file_format(file_obj)
	return flag


if __name__ == '__main__':
	with open(PATH, 'r') as file_obj:
		if file_is_valid(file_obj, PATH):
			print [list(l) for l in get_list(PATH)]
		else:
			print 'Invalid file type or format'
