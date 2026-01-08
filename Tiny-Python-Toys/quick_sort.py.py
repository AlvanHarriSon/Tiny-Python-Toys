def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # 选择中间的元素作为基准
        left = [x for x in arr if x < pivot]  # 小于基准的元素
        middle = [x for x in arr if x == pivot]  # 等于基准的元素
        right = [x for x in arr if x > pivot]  # 大于基准的元素
        return quicksort(left) + middle + quicksort(right)

# 示例使用
arr = [111,3,555,66666,333333333,5,8,2222]
sorted_arr = quicksort(arr)
print(sorted_arr)
