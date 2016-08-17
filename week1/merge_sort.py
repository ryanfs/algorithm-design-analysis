# test = [1, 20, 6, 4, 5] # should be 5
# test_sorted_arr = [1, 2, 3, 5] # should be 0
count = 0
def merge_sort(arr):
  if len(arr) < 2:
    return arr
  middle = len(arr) / 2
  left = arr[:middle]
  right = arr[middle:]
  return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    global count
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            print 'right!'
            count = count + (len(left) - i)
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
# print merge_sort(test_sorted_arr)
# print count

fname = 'ints.txt'
with open(fname) as f:
    integers = f.readlines()
    merge_sort(integers)
    print count
