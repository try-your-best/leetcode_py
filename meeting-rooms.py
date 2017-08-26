# -*- coding: utf-8 -*-

# Time:  O(nlogn)
# Space: O(n)
#
# Definition for an interval.

class Interval:
	def __init__(self, s=0, e=0):
			self.start = s
			self.end = e


# class Solution:
# 		# @param {Interval[]} intervals
# 		# @return {boolean}
# 		def canAttendMeetings(self, intervals):
# 			if len(intervals) <= 1:
# 				return True
# 			intervals.sort(key=lambda x: x.start)
# 			for index in xrange(len(intervals)-1):
# 				if intervals[index].end > intervals[index+1].start:
# 					return False
#
# 			return True


class Solution:
	# @param {Interval[]} intervals
	# @return {boolean}
	def canAttendMeetings(self, intervals):
		intervals.sort(key=lambda x: x.start)

		for i in xrange(1, len(intervals)):
			if intervals[i].start < intervals[i - 1].end:
				return False
		return True


if __name__ == "__main__":
	intervals = []
	# intervals = [Interval(1, 4)]
	# intervals = [Interval(1, 4), Interval(3, 5)]
	# intervals = [Interval(1, 4), Interval(4, 5)]
	# intervals = [Interval(1, 4), Interval(5, 5)]
	print Solution().canAttendMeetings(intervals)