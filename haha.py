# write a quick sort function
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        print('aaaaa')
        return quick_sort(less) + [pivot] + quick_sort(greater)
        
