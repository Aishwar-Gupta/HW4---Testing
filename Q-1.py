import unittest

def someSort(arr):
	n = len(arr)        # Removed +1 as it would increase the actual array length by 1
	for i in range(n):
		swapped = True
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if swapped == False:
			break

covid = [88,85,123,96,104,81]
someSort(covid)
print(covid)

#----------------------------------Unit Tests-----------------------------------

def test_someSort_pos():
	covid = [88,85,123,96,104,81]
	someSort(covid)
	expect = [81,85,88,96,104,123]
	assert covid == expect


def test_someSort_neg():
	covid = [-88,-85,-123,-96,-104,-81]
	someSort(covid)
	expect = [-123,-104,-96,-88,-85, -81]
	assert covid == expect

