nums = [5, 15, 3, 8, 6]


def get_index_small_value(nums, current_index):
    small = current_index
    for i in range(current_index + 1, len(nums)):
        if nums[small] > nums[i]:
            small = i
    return small

print(get_index_small_value(nums, 3))
for i in range(len(nums)):
    index = get_index_small_value(nums, i)
    if i != index:
        nums[i], nums[index] = nums[index], nums[i]
        print(nums)
print(nums)