# Simple Function Arguments and Prime Numbers
# ==========================================

def isPrime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# =============================================================================
# WAYS TO PASS ARGUMENTS TO FUNCTIONS (Simple Examples)
# =============================================================================

# 1. Normal Arguments (in order)
def add_numbers(a, b):
    return a + b

# 2. Default Arguments (has default value)
def greet(name, message="Hello"):
    return f"{message} {name}!"

# 3. Keyword Arguments (use parameter names)
def introduce(name, age, city):
    return f"I am {name}, {age} years old from {city}"

# 4. Many Arguments (*args)
def sum_many(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# =============================================================================
# PRIME NUMBERS IN RANGE - SIMPLE FUNCTIONS
# =============================================================================

# Simple function - just give start and end
def show_primes(start, end):
    """Show all prime numbers between start and end"""
    print(f"Prime numbers from {start} to {end}:")
    primes = []
    
    for num in range(start, end + 1):
        if isPrime(num):
            primes.append(num)
    
    print(primes)
    return primes

# Function with default values
def show_primes_easy(start=1, end=20):
    """Show primes with default range 1 to 20"""
    return show_primes(start, end)

# Function to check many numbers at once
def check_many_primes(*numbers):
    """Check if many numbers are prime"""
    results = []
    for num in numbers:
        results.append(isPrime(num))
    return results

# =============================================================================
# EXAMPLES
# =============================================================================

print("Function Examples:")

# 1. Normal arguments
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")

# 2. Default arguments
print(greet("John"))           # Uses default "Hello"
print(greet("Mary", "Hi"))     # Uses custom "Hi"

# 3. Keyword arguments
print(introduce(city="Mumbai", name="Ram", age=25))

# 4. Many arguments
print(f"Sum of 1,2,3,4,5 = {sum_many(1,2,3,4,5)}")

print("\nPrime Numbers Examples:")

# Show primes in range
show_primes(10, 30)

# Use default range
show_primes_easy()

# Custom range
show_primes_easy(50, 70)

# Check specific numbers
test_numbers = [2, 5, 10, 13, 17, 20]
results = check_many_primes(*test_numbers)

print("Number | Is Prime?")
print("-" * 18)
for num, is_prime in zip(test_numbers, results):
    print(f"{num:6} | {is_prime}")