# Practical No. 3: Greedy Algorithm - Selection Sort
# 💡 Greedy Strategy: At each step, select the smallest element from the unsorted portion and move it to its correct position.

def selection_sort(arr):
    n = len(arr)
    print("🔢 Original Array:", arr)
    
    for i in range(n):
        min_index = i
        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i+1}: {arr}")

    return arr

# Example input array
arr = [64, 25, 12, 22, 11]

# Perform Selection Sort
sorted_arr = selection_sort(arr)

print("\n✅ Sorted Array (Greedy Selection Sort):", sorted_arr)
