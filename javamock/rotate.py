nums = [1,2,3,4,5,6,7,8,9,10]
even_elements = []

for i in range(len(nums)):
    if i % 2 == 0:
        even_elements.append(i)

print(nums)
k = int(input("enter the number: "))

k = k % len(nums)

l, r = 0, len(nums) - 1

while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
print(nums)

l, r = 0, k - 1
while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1
print(nums)

l, r = k, len(nums) - 1
while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


print(nums)











# k = 2

# print(nums)
#
# k = k % len(nums)
#
# l, r = 0, len(nums) - 1
#
# while l < r:
#     nums[l], nums[r] = nums[r], nums[l]
#     l, r = l + 1, r - 1
# print(nums)
#
#
# while l < r:
#     l, r = l = 0, k - 1
#     nums[l], nums[r] = nums[r], nums[l]
# print(nums)
# while l < r:
#     l, r = k, len(nums) - 1
#     nums[l], nums[r] = nums[r], nums[l]
# print(nums)









# 0 1 2 3 4
# 1 2 3 4 5
# 1   3   5
# 5 2 1 4 3