def mergeIntervals(intervals):
  if intervals:
    merged = []
    intervals.sort(key = lambda x:x[0])
    for i in intervals:
      if not merged or merged[-1][1] < i[0]:
        merged.append(i)
      else:
        merged[-1][1] = max(i[1], merged[-1][1])
    return merged

res = mergeIntervals([[1,3], [2,6], [8,10], [15,18]])
print(res)



# out = []
#     for i in sorted(intervals, key=lambda i: i.start):
#         if out and i.start <= out[-1].end:
#             out[-1].end = max(out[-1].end, i.end)
#         else:
#             out += i,
#     return out
