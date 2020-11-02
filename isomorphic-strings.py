# -*- coding: utf-8 -*-
__author__ = 'DamonHao'


"""
同构字符串

这道题让我们求同构字符串，就是说原字符串中的每个字符可由另外一个字符替代，
可以被其本身替代，相同的字符一定要被同一个字符替代，且一个字符不能被多个字符替代，
即不能出现一对多的映射。根据一对一映射的特点，我们需要用两个哈希表分别来记录原字符串和目标字符串中字符出现情况，
由于ASCII码只有256个字符，所以我们可以用一个256大小的数组来代替哈希表，并初始化为0，我们遍历原字符串，
分别从源字符串和目标字符串取出一个字符，然后分别在两个哈希表中查找其值，若不相等，则返回false，若想等，将其值更新为i + 1，代码如下：

根据一对一映射的特点， 没绑定过的映射值为0，绑定完后给设置一个映射值
注意定义： Two strings are isomorphic if the characters in s can be replaced to get t.

'abc', 'dae' 是 true，a->d, b->a, 一一映射。所以要两个哈希表

Time:  O(n)
Space: O(1)

"""


class Solution(object):

	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(s) != len(t):
			return False

		lookUp1, lookUp2 = [0] * 256, [0] * 256
		idx = 0
		for char1, char2 in zip(s, t):
			if lookUp1[ord(char1)] != lookUp2[ord(char2)]:
				return False
			idx += 1
			lookUp1[ord(char1)] = idx
			lookUp2[ord(char2)] = idx

		return True

if __name__ == "__main__":
	print Solution().isIsomorphic('egg', 'abb')
	print Solution().isIsomorphic('foo', 'bar')
	print Solution().isIsomorphic('paper', 'title')

	print Solution().isIsomorphic('abc', 'dae')
