# -*- coding: utf-8 -*-
__author__ = 'DamonHao'

"""
这种考核概率很小
"""


class Solution:

	def countPrimes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		if n < 3:
			return 0
		primes = [True] * n
		primes[0] = primes[1] = False
		for i in range(2, int(n ** 0.5) + 1):
			if primes[i]:
				primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
		return sum(primes)