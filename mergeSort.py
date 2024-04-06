unsorted_list = [8,5,3,10,4,9,7,1,2,6]

def merge_sort(li, level=0):
    if len(li) == 1:
        return li

    mid_point = len(li)//2
    left_half = li[0:mid_point]
    right_half = li[mid_point:len(li)]

    left_sorted = merge_sort(left_half, level=level+1)
    right_sorted = merge_sort(right_half, level=level+1)

    print(f'{level=}\t{li}')

    is_sorted = False
    merged_list = []
    left_position = 0
    right_position = 0
    while not is_sorted:

        if left_position >= len(left_sorted):
            merged_list = merged_list + right_sorted[right_position:]
            break
        if right_position >= len(right_sorted):
            merged_list = merged_list + left_sorted[left_position:]
            break

        if left_sorted[left_position] < right_sorted[right_position]:
            merged_list.append(left_sorted[left_position])
            left_position += 1
        else:
            merged_list.append(right_sorted[right_position])
            right_position += 1

    return merged_list

print(merge_sort(unsorted_list))