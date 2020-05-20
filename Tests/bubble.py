def bubble_sort(arr):
  for i in range(len(arr)):
    for idx in range(len(arr) - i - 1):
      if arr[idx] > arr[idx + 1]:
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
my_nums = [7, 3, 4, 2]

print(bubble_sort(my_nums))

