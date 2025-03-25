def fibonacci(n):
    sequence = [0, 1]  # Pehle do numbers fix hain
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]  # Pichle do numbers ka sum
        sequence.append(next_number)
    return sequence[:n]  # Sirf n numbers return karna

# User Input
num = int(input("Enter the number of Fibonacci terms: "))

# Valid Input Check
if num <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Sequence:", fibonacci(num))
