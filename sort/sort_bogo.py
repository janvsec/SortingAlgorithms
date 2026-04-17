import random
import time

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def bogosort(lst):
    attempts = 0
    while not is_sorted(lst):
        random.shuffle(lst)
        attempts += 1
    return lst, attempts

# Load numbers from file
with open('intlist.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f if line.strip()]

start_time = time.time()

sorted_numbers, attempts = bogosort(numbers)

end_time = time.time()
duration = end_time - start_time

# Save results
with open('bogosort.txt', 'w') as f:
    f.write("Sorted numbers:\n")
    for num in sorted_numbers:
        f.write(f"{num}\n")
    
    f.write(f"\nTime taken: {duration:.6f} seconds\n")
    f.write(f"Shuffle attempts: {attempts}\n")

print("Done. Check bogosort.txt")
