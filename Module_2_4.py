numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()
for i in range(len(numbers)):
    Nat_Del = int(0) # счетчик натуральных делителей
    for j in numbers[0:(i+1)]:
        if numbers[i] % j == 0:
            Nat_Del = Nat_Del + 1
    if Nat_Del==2:
        primes.append(numbers[i])
    elif Nat_Del > 2:
        not_primes.append(numbers[i])
print('Список простых чисел:',primes)
print('Список не простых чисел:',not_primes)
