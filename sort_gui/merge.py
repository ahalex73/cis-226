
def merge_sort(array):
    ''' Sorts a given array with merge sort O(n log(n))'''
    if len(array) <= 1:
        return array

    midpoint = int(len(array) / 2)

    left, right = merge_sort(array[:midpoint]), merge_sort(array[midpoint:])

    return merge(left,right)

def merge(left, right):
    results = []
    left_pointer = right_pointer = 0

    
    while left_pointer < len(left) and right_pointer < len(right):

        if left[left_pointer] < right[right_pointer]:

            results.append(left[left_pointer])
            left_pointer += 1
            
        else:
            results.append(right[right_pointer])
            right_pointer += 1


    results.extend(left[left_pointer:])
    results.extend(right[right_pointer:])
    
    return results

def main():
    array = [5, 4, 3, 2, 1]
    print(array)

    result = merge_sort(array)
    print(result)


if __name__ == '__main__':
    main()

