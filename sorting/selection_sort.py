def selection_sort(numbers):

    for i in range(len(numbers)):
        lowest_value_in_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[lowest_value_in_index]:
                lowest_value_in_index = j

            numbers[i], numbers[lowest_value_in_index] = numbers[lowest_value_in_index], numbers[i]

    return numbers