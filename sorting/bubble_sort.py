def bubble_sort(numbers):

    swapped = True # run at least once
    while swapped:
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i] # swapping magic
                swapped = True

    return numbers