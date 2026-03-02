nums = [10,20,30,40,50]
even_numbers = []

print(nums)
for i in range(len(nums)):
    if i % 2 == 0:
        even_numbers.append(nums[i])

print(even_numbers)

k = int(input("enter number: "))
k = k % len(even_numbers)

l,r = 0, len(even_numbers) - 1
while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l, r = l + 1, r - 1
print(even_numbers)


l,r = 0, k - 1
while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l, r = l + 1, r - 1
print(even_numbers)

l,r = k, len(even_numbers) - 1
while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l, r = l + 1, r - 1
print(even_numbers)


even_pointer = 0

for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = even_numbers[even_pointer]
        even_pointer += 1

print(nums)









# evn_pointers = 0
#
# for i in range(len(nums)):
#     if i % 2 == 0:
#         nums[i] = even_numbers[evn_pointers]
#         evn_pointers += 1
#
# print(nums)
































# 1234
# 4231
# 4123
# print(even_numbers)
#
#
# 12345
# 54321
# 45321
# 45123
#
# 12345
# 52341
# 52341
# 51234
#
#
#
# 1 2 3 4 5 6 7 8 9 10
#
# 10 9 8 7 6 5 4 3 2 1
#
# 8 9 10, 4 5 6 7 3 2 1
#
# 8 9 10. 1 2 3 4 5 6 7