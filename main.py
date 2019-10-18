

def quick_sort(array):
	quick_sort_core(array, 0, len(array)-1)
	return array


def quick_sort_core(array, left, righ):
	if left < righ:
		p = partition(array, left, righ)
		quick_sort_core(array, left, p-1)
		quick_sort_core(array, p+1, righ)


def partition(array, left, righ):
	pivot = array[righ]
	i = left - 1
	for j in xrange(left, righ):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]

	i += 1
	array[i], array[righ] = array[righ], array[i]

	return i


if __name__ == '__main__':
	array = [4, 3, 1, 2]
	print quick_sort(array)