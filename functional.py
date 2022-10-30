def flatten_and_sort(arr):
    out = []
    for item in arr:
        if type(item) == list:
            for i in item:
                out.append(i)
        else:
            out.append(item)
    return sorted(out)


print(flatten_and_sort([1, [2, 5, 4], 3, 9, 2, [55, 22]]))
