

def quick_sort(ary, left, right):
	if left < right:
		mid = partition(ary, left, right)
		quick_sort(ary, left, mid-1)
		quick_sort(ary, mid+1, right)


def partition(ary, left, right):
	pivot = ary[right]
	i = left-1
	for j in range(left, right):
		if ary[j] <= pivot:
			i+=1
			ary[i], ary[j] = ary[j], ary[i]

	i+=1
	ary[i], ary[right] = ary[right], ary[i]
	return i



# ary = [4, 3, 2, 1]
# quick_sort(ary, 0, len(ary)-1)
# print ary
#
#
# ary = [4, 3]
# quick_sort(ary, 0, len(ary)-1)
# print ary
#
#
# a = {}
# a.get()


s = '您好'
# print(len(s))
# print(s.encode('utf-8'))
# print(len(s.encode('utf-8')))
# print(type(s))
print(s[:2])
print(s[:1])
print(s[1:])
print(s[1:-1])
print(s[:-1])
