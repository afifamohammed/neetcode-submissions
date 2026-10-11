"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        # Optimal Solution

        intervals.sort(key = lambda x : x.start) 

        # 'key' tells sort() what value to use for sorting.
        # 'lambda' creates a short, temporary one-line function.
        # Syntax: lambda x(input) : value to sort by (output)

        for i in range(1,len(intervals)):

            if intervals[i].start < intervals[i-1].end:
                return False

            # interval is given as class, and have objects as (start, end) of intervals

        return True

