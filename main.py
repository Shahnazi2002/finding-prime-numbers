number = int(input('Enter a number and I will calculate all prime numbers less than or equal to it.'))

numbers = [i for i in range(2, number+1)]
primeNumbers = []
for i in numbers:
    primeNumbers.append(i)
    for j in numbers:
        if j not in primeNumbers and j%i == 0:
            numbers.remove(j)
print(primeNumbers)
