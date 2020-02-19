# -*- coding: utf-8 -*-

# http://www.cnblogs.com/grandyang/p/5244720.html
# https://github.com/kamyu104/LeetCode/blob/master/Python/meeting-rooms-ii.py

# Time:  O(nlogn)
# Space: O(n)

# Definition for an interval.
class Interval:

	def __init__(self, s=0, e=0):
			self.start = s
			self.end = e


class Solution:
	# @param {Interval[]} intervals
	# @return {integer}
	def minMeetingRooms(self, intervals):
		starts, ends = [], []
		for interval in intervals:
			starts.append(interval.start)
			ends.append(interval.end)

		starts.sort()
		ends.sort()

		s, e = 0, 0
		min_rooms, cnt_rooms = 0, 0

		starts_len = len(starts)
		while s < starts_len:
			if starts[s] < ends[e]:
				cnt_rooms += 1  # 如果当前会议的开始时间比当前会议结束时间小，则要开启一个房间。 注意，这里的开始和结束时间不一定是同一个会议的。
				min_rooms = max(min_rooms, cnt_rooms)
				s += 1
			else:
				cnt_rooms -= 1  # 如果当前会议的开始时间比当前会议结束时间大，则要减去一个房间，
				e += 1

		return min_rooms


if __name__ == "__main__":
	intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
	print(Solution().minMeetingRooms(intervals))

