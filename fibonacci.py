n = int(input('Podaj nr, dla którego chcesz odczytać wartość z ciągu Fibonacciego: '))


def fibonacci_number(numbers):
    fibb = [0, 1]
    while numbers >= len(fibb):
        fibb.append(fibb[-1] + fibb[-2])
    return fibb


fibb = fibonacci_number(n)
print(fibb)
print(f'Nr {n} ciągu Fibonacciego to {fibb[n]}.')

for i in fibb:
    print(i, end=" ")