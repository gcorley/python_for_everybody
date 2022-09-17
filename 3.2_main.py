import re

# sample sum = 445833
# actual sum ends with 824

# handle = open('sample_data.txt')
handle = open('actual_data.txt')
data = handle.read()
nums = re.findall(r'\d+', data)
total = 0
for num in nums:
    total += int(num)
print(total)
