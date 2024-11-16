def is_perfect_number(num):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

print("Perfect numbers between 1 and 100:")
for number in range(1, 101):
    if is_perfect_number(number):
        print(number, end=" ")