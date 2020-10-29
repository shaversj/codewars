def sum_of_intervals(intervals: list):
    if len(intervals) == 1:
        return intervals[0][1] - intervals[0][0]

    list_of_intervals = [list(interval) for interval in intervals]
    sorted_intervals = sorted(list_of_intervals, key=lambda x: x[0])

    idx = 0

    while idx != len(sorted_intervals):
        if idx == 0:
            idx += 1
            continue
        else:
            prev_end = sorted_intervals[idx - 1][1]
            new_begin = sorted_intervals[idx][0]
            new_end = sorted_intervals[idx][1]
            if new_begin > prev_end:
                idx += 1
                continue
            else:
                print(sorted_intervals, idx)
                print(new_end, prev_end)
                sorted_intervals[idx - 1][1] = max(new_end, prev_end)
                sorted_intervals.pop(idx)

    counter = 0
    for interval in sorted_intervals:
        counter += interval[1] - interval[0]

    return counter




# print(sum_of_intervals([
#     [1, 2],
#     [6, 10],
#     [11, 15]
# ]))  # => 9
#
# print(sum_of_intervals([
#     [1, 4],
#     [7, 10],
#     [3, 5]
# ]))  # ; // => 7
#
# print(sum_of_intervals([
#     [1, 5],
#     [10, 20],
#     [1, 6],
#     [16, 19],
#     [5, 11]
# ]))  # ; // => 19

# print(sum_of_intervals(intervals=i))

print(sum_of_intervals([[-11, 92], [142, 452], [326, 426], [365, 386]]))