"""
https://www.cnblogs.com/grandyang/p/5192426.html
"""

class Solution(object):
	# @param {string[]} words
	# @param {string} word1
	# @param {string} word2
	# @return {integer}
	def shortestDistance(self, words, word1, word2):
		p1 = None
		p2 = None
		min_dis = len(words)
		if word1 == word2:
			for idx, w in enumerate(words):
				if w == word1:
					if p1 is not None:
						min_dis = min(min_dis, idx - p1)
					p1 = idx
		else:
			for idx, w in enumerate(words):
				flag = False
				if w == word1:
					p1 = idx
					flag = True
				elif w == word2:
					p2 = idx
					flag = True
				if flag and p1 is not None and p2 is not None:
					min_dis = min(min_dis, abs(p1-p2))
		return min_dis


if __name__ == '__main__':
	sl = Solution()
	print(sl.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'coding'))
	print(sl.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'makes', 'makes'))