def list_of_sum(number):
    numbers = [1, 2]
    while len(numbers) <= number:
        numbers.append(sum(numbers))
    return numbers


print(list_of_sum(10))