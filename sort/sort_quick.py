import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

with open('intlist.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

start_time = time.time()

sorted_numbers = quicksort(numbers)

end_time = time.time()
duration = end_time - start_time

with open('quicksort.txt', 'w') as f:
    for num in sorted_numbers:
        f.write(f"{num}\n")
    f.write(f"\nTime taken: {duration:.6f} seconds\n")

print("Done. Check quicksort.txt")
