class SelectionSort:
    def selection_sort(li):
        for i in range(len(li)-1, 0, -1):
            pos_max = 0
            for loc in range(1, i+1):
                if(li[loc] > li[pos_max]):
                    pos_max = loc

            temp = li[i]
            li[i] = li[pos_max]
            li[pos_max] = temp

        return li
