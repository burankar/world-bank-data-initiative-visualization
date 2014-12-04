'''
The MIT License (MIT)
Copyright (c) 2014 Brian Urankar
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
'''
This code is pulled and adopted from the newcoder.io dataviz tutorial. 
I will update this attribution later in the project.
'''

import csv
MY_FILE = 'WDI_csv/WDI_Data.csv'


def parse(raw_file, delimiter):
	"""Parses the raw WDI_Data.csv to a JSON-LINE object."""
	
	#open CSV file
	opened_file = open(raw_file)

	#read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimiter)

	#build a data structure to return parsed_data
	parsed_data = []
	fields = csv_data.next()

	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	#close CSV file
	opened_file.close()
	
	return parsed_data