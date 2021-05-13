import unittest

import math, sys, contextlib
from io import StringIO


def printGraph(data):
	out = []
	for i in data:
		t = []
		for x in range(i):
			print ('x', end='')
			t.append('x')        # added 'x' to be appended to the tuple
		print ()
		out.append(t)        # changed extends to append to add the lists rather than each value to same list
	return out

data = [1,2,3]
output = printGraph(data)
print(output)


#-------------------------------------------Unit Tests---------------------------------------------


def test_printGraph():
	data = [1,2,3]
	output = printGraph(data)
	expect = [['x'], ['x','x'], ['x','x','x']]
	assert  output == expect


def test_printGraph_1():
	data = [3,2,1]
	output = printGraph(data)
	expect = [['x','x','x'], ['x','x'], ['x']]
	assert output == expect


def captured_output():        # collects the output including the pattern of 'x'
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def test_3():
	data = [1, 2, 3, 5]
	expect = [['x'], ['x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		output = printGraph(data)
	output_1 = temp_stdout.getvalue().strip()
	assert output_1 == "x\nxx\nxxx\nxxxxx"
	assert output == expect


def test_4():
	data = [5, 3, 2, 1]
	expect = [['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x'], ['x']]
	temp_stdout = StringIO()
	with contextlib.redirect_stdout(temp_stdout):
		output = printGraph(data)
	output_1 = temp_stdout.getvalue().strip()
	assert output_1 == "xxxxx\nxxx\nxx\nx"
	assert output == expect
