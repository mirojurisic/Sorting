sleep_times = [(24, 13), (21, 55), (23, 20), (22, 5), (24, 23), (21, 58), (24, 3)]


def bubble_sort_2(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - 1):
            if l[j][0] < l[j + 1][0] or (l[j][0] == l[j + 1][0] and l[j][1] < l[j + 1][1]):
                l[j], l[j + 1] = l[j + 1], l[j]


bubble_sort_2(sleep_times)
print(sleep_times)
print("Pass" if (sleep_times == [(24, 23), (24, 13), (24, 3), (23, 20), (22, 5), (21, 58), (21, 55)]) else "Fail")
