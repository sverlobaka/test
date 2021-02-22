def counting_sort(numbers):
    
    max_numbers = max(numbers)
    counters = [0] * (max_numbers + 1)

    for i in range(len(numbers)):
        counters[numbers[i]] += 1

    pos = 0
    for j in range(len(counters)):
        for i in range(counters[j]):
            numbers[pos] = j
            pos += 1

    return counters
