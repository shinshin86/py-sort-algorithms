class CountingSort:
    def counting_sort(li):
        maxval = max(li)
        count = [0] * (maxval + 1)

        for a in li:
            count[a] += 1
        i = 0

        for a in range(maxval + 1):
            for c in range(count[a]):
                li[i] = a
                i += 1
        return li
