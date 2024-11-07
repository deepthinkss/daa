import random


class QuickSort:
    def __init__(self, array):
        self.array = array

    # Deterministic method to find pivot
    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1

        for j in range(low, high):
            if self.array[j] <= pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]

        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        return i + 1

    # Randomized method to find pivot
    def partition_random(self, low, high):
        pivot = random.randint(low, high)
        self.array[pivot], self.array[high] = self.array[high], self.array[pivot]
        return self.partition(low, high)

    # Deterministic variant of sort
    def sort_d(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.sort_d(low, pivot - 1)
            self.sort_d(pivot + 1, high)

    # Randomized variant of sort
    def sort_r(self, low, high):
        if low < high:
            pivot = self.partition_random(low, high)
            self.sort_r(low, pivot - 1)
            self.sort_r(pivot + 1, high)


# Main program
array = [int(i) for i in input("Enter array elements separated by spaces: ").split()]

# Deterministic variant of sort
sort_deterministic = QuickSort(array.copy())
sort_deterministic.sort_d(0, len(array) - 1)
print("Sorted array (Deterministic QuickSort):", sort_deterministic.array)

# Randomized variant of sort
sort_randomized = QuickSort(array.copy())
sort_randomized.sort_r(0, len(array) - 1)
print("Sorted array (Randomized QuickSort):", sort_randomized.array)
