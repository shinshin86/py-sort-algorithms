class QuickSort:
    def quick_sort(li):
        QuickSort.quick_sort_helper(li, 0, len(li) - 1)
        return li

    def quick_sort_helper(li, first, last):
        if first < last:
            splitpoint = QuickSort.partition(li, first, last)
            QuickSort.quick_sort_helper(li, first, splitpoint - 1)
            QuickSort.quick_sort_helper(li, splitpoint + 1, last)

    def partition(li, first, last):
        pivot_value = li[first]

        left_mark = first + 1
        right_mark = last

        done = False
        while not done:
            while left_mark <= right_mark and li[left_mark] <= pivot_value:
                left_mark = left_mark + 1

            while li[right_mark] >= pivot_value and right_mark >= left_mark:
                right_mark = right_mark - 1

            if right_mark < left_mark:
                done = True
            else:
                temp = li[left_mark]
                li[left_mark] = li[right_mark]
                li[right_mark] = temp
        temp = li[first]
        li[first] = li[right_mark]
        li[right_mark] = temp

        return right_mark
