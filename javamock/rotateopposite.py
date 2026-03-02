

nums = [10,20,30,40,50]
print(nums)
even_numbers = []
for i in range(len(nums)):
    if i % 2 == 0:
        even_numbers.append(nums[i])
print(even_numbers)

k = int(input("enter number: "))
n = len(nums)
k = k % n
k = n - k

l,r, = 0, len(even_numbers) - 1

while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l, r = l + 1, r - 1
print(even_numbers)

l,r = 0, k -1
while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l, r = l + 1, r - 1
print(even_numbers)

l, r = k, len(even_numbers) - 1
while l < r:
    even_numbers[l], even_numbers[r] = even_numbers[r], even_numbers[l]
    l,r = l + 1, r - 1
print(even_numbers)

even_pointer = 0

for i in range(len(nums)):
    if i % 2 == 0:
        nums[i] = even_numbers[even_pointer]
        even_pointer += 1
print(nums)

