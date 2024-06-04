
from merge_sort_HW3 import merge_sort
from insertion_sort_HW3 import insertion_sort
from generate_data_HW3 import generate_data
from measure_time_HW3 import measure_time

data_sizes = [1000, 5000, 10000, 50000, 100000]

# Тестові дані для алгоритмів
test_data = {size: generate_data(size) for size in data_sizes}

results = {}

for size in data_sizes:
    data = test_data[size]
    results[size] = {
        'merge_sort': measure_time(merge_sort, data),
        'insertion_sort': measure_time(insertion_sort, data),
        'timsort': measure_time(sorted, data)
    }

# Виведення результатів
for size, timings in results.items():
    print(f"Data size: {size}")
    for sort_name, timing in timings.items():
        print(f"{sort_name}: {timing:.6f} seconds")
    print()
