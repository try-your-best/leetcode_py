# -*- coding: utf-8 -*-
__author__ = 'damon'


class Solution(object):
		def isStrobogrammatic(self, num: str):
			l = 0
			r = len(num) -1
			look_up = set(['0', '1', '8'])
			while l <= r:
				if num[l] == num[r]:
					if num[l] not in look_up:
						return False
				else:
					if not ((num[l] == '6' and num[r] == '9') or (num[l] == '9' and num[r] == '6')):
						return False
				l+=1
				r-=1
			return True


class Solution(object):
	def isStrobogrammatic(self, num: str):
		l = 0
		r = len(num) - 1
		look_up = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
		while l <= r:
			if num[l] not in look_up or look_up[num[l]] != num[r]:
				return False
			l += 1
			r -= 1
		return True


if __name__ == '__main__':
	sl = Solution()
	print(sl.isStrobogrammatic('69'))
	print(sl.isStrobogrammatic('88'))
	print(sl.isStrobogrammatic('962'))