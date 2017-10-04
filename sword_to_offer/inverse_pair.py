# -*- coding: utf-8 -*-


def inversePairsCore(data, copyData, start, end):
	if start == end:
		copyData[start] = data[start]
		return 0

	halfDataLen = (end-start)/2

	# 这里 data 和 copyData 交换位置是因为， 每次 data 保证两个分组是有序的， 而 copyData 是整组有序
	# 这样处理主要是为了避免重复的创建辅助序列
	left = inversePairsCore(copyData, data, start, start+halfDataLen)
	right = inversePairsCore(copyData, data, start+halfDataLen+1, end)

	i = start + halfDataLen
	j = end
	indexCopy = end
	count = 0

	while i >= start and j >= start+halfDataLen+1:
		if data[i] > data[j]:
			copyData[indexCopy] = data[i]
			indexCopy -= 1
			i -= 1
			count += j - start - halfDataLen
		else:
			copyData[indexCopy] = data[j]
			indexCopy -= 1
			j -= 1

	while i >= start:
		copyData[indexCopy] = data[i]
		indexCopy -= 1
		i -= 1

	while j >= start+halfDataLen+1:
		copyData[indexCopy] = data[j]
		indexCopy -= 1
		j -= 1

	return left + right + count


def inversePairs(data):
	if not data:
		return 0

	copyData = [num for num in data]
	return inversePairsCore(data, copyData, 0, len(data)-1)


if __name__ == '__main__':
	print inversePairs([7, 5, 6, 4])
	print inversePairs([1, 2, 3, 4])
	print inversePairs([1, 2, 4, 3])
