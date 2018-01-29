class BubbleSort:
    def bubble_sort(li):
        for p in range(len(li)-1, 0, -1):
            for i in range(p):
                if li[i] > li[i+1]:
                    temp = li[i]
                    li[i] = li[i+1]
                    li[i+1] = temp
        return li

    def short_bubble_sort(li):
        exchanges = True
        p = len(li) - 1
        while p > 0 and exchanges:
            exchanges = False
            for i in range(p):
                if(li[i] > li[i+1]):
                    exchanges = True
                    temp = li[i]
                    li[i] = li[i+1]
                    li[i+1] = temp
            p = p-1
        return li
