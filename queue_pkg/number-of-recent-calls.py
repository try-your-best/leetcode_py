# -*- coding: utf-8 -*-
__author__ = 'damon'

import collections


class RecentCounter:

	def __init__(self):
		self.__q = collections.deque()

	def ping(self, t: int) -> int:
		self.__q.append(t)
		while self.__q[0] < t - 3000:
			self.__q.popleft()
		return len(self.__q)
