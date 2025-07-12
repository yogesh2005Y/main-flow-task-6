def merge_intervals(intervals):
 if not intervals:
    return []

 intervals.sort()
 merged = [intervals[0]]

 for start, end in intervals [1:]:
    last_end = merged[-1][1]
    if start <= last_end:
         merged[-1][1] = max(end, last_end)
    else:
         merged.append([start, end])
    return merged

n = int(input("Enter number of intervals: "))
intervals = [list(map(int, input(f"Interval {i+1}: ").split())) for i in range(n)]
print("Merged intervals:", merge_intervals(intervals))