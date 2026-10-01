from typing import List


def reverse_list(arr: List[int]) -> List[int]:

    new_arr = []
    n = len(arr)

    for i in range(n):
        new_arr.append(arr.pop())

    return new_arr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
