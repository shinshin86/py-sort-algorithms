class MergeSort:
    def merge_sort(li):
        if len(li) > 1:
            mid = len(li) // 2
            left_half = li[:mid]
            right_half = li[mid:]

            # print("------------> debug")
            # print("left_half : ", left_half)
            # print("right_half : ", right_half)

            MergeSort.merge_sort(left_half)
            MergeSort.merge_sort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    li[k] = left_half[i]
                    i = i + 1
                else:
                    li[k] = right_half[j]
                    j = j + 1
                k = k + 1

            while i < len(left_half):
                li[k] = left_half[i]
                i = i + 1
                k = k + 1

            while j < len(right_half):
                li[k] = right_half[j]
                j = j + 1
                k = k + 1
        return li
