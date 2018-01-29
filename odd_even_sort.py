class OddEvenSort:
    def odd_even_sort(li):
        n = len(li)
        is_sorted = 0
        while is_sorted == 0:
            is_sorted = 1
            for i in range(1, n-1, 2):
                if li[i] > li[i+1]:
                    li[i], li[i+1] = li[i+1], li[i]
                    is_sorted = 0

            for i in range(0, n-1, 2):
                if li[i] > li[i+1]:
                    li[i], li[i+1] = li[i+1], li[i]
                    is_sorted = 0
        return li
