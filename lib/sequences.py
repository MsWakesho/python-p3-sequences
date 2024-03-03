def print_fibonacci(length):
    fibonacci_list = [0, 1]
    for i in range(2, length):
        next_fibonacci = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_fibonacci)
    print(fibonacci_list)

print_fibonacci(9)
