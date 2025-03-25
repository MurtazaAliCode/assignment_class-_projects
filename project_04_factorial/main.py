import math

def calculate_factorial(n):
    try:
        n = int(n)
        if n < 0:
            return "Factorial is not defined for negative numbers."
        return math.factorial(n)
    except ValueError:
        return "Please enter a valid integer."

# User input
number = input("Enter a number: ")

# Calculate factorial
result = calculate_factorial(number)

# Display result
print(f"Factorial: {result}")

# Display factorial formula if input is valid
if number.isdigit() and int(number) >= 0:
    num = int(number)
    formula = f"{num}! = " + " × ".join(map(str, range(num, 0, -1))) + f" = {result}"
    print("Factorial Formula:", formula)
