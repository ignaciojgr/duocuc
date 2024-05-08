array=[396,77,493,282,304,120,878,747,212,802,525,661,623,226,870,178,79,513,457,908,243,953,60,94,24,664,553,450,794,60,102,540,471,577,114,60,870,1,84,368,519,644,936,699,737,747,794,802,870,870,878,908,936,953,]
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
print(bubble_sort(array))