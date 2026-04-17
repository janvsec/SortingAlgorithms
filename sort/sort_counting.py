import time

with open('intlist.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

start_time = time.time()

count = {}
for num in numbers:
    count[num] = count.get(num, 0) + 1

sorted_numbers = []
for num in sorted(count):
    sorted_numbers.extend([num] * count[num])

end_time = time.time()
duration = end_time - start_time

with open('countingsort.txt', 'w') as f:
    for num in sorted_numbers:
        f.write(f"{num}\n")
    f.write(f"\nTime taken: {duration:.6f} seconds\n")

print("Done. Check countingsort.txt")
