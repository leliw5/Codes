numbers = [1, 3, 5, 2, 8, 9, 10, 11, 12, 20]
average = []
n = 1
i = 0

while len(average) < len(numbers):
    average.append((sum(numbers[i-n:i]) + sum(numbers[i:i+n+1])) / (len(numbers[i-n:i]) + len(numbers[i:i+n+1])))
    i += 1

print(average)