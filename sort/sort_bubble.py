import time

with open('intlist.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

start_time = time.time()

n = len(numbers)
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

end_time = time.time()
duration = end_time - start_time

with open('bubblesort.txt', 'w') as f:
    for num in numbers:
        f.write(f"{num}\n")
    f.write(f"\nTime taken: {duration:.6f} seconds\n")

print("Done. Check bubblesort.txt")
