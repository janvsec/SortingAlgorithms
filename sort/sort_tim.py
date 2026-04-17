import time

with open('intlist.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

start_time = time.time()

numbers.sort()

end_time = time.time()
duration = end_time - start_time

with open('timsort.txt', 'w') as f:
    for num in numbers:
        f.write(f"{num}\n")
    f.write(f"\nTime taken: {duration:.6f} seconds\n")

print("Done. Check timsort.txt")
