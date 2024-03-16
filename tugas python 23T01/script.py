# Function to check if a number is odd or even
def is_odd_or_even(number):
    # If the remainder of the division by 2 is 0, then the number is even
    if number % 2 == 0:
        return "genap"
    # Otherwise, the number is odd
    else:
        return "ganjil"

# Example usage
number1 = 15  # odd number
number2 = 12  # even number

# Perform arithmetic operations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
modulus = number1 % number2

# Print out the results
print(f"Hasil penjumlahan: {number1} + {number2} = {addition}")
print(f"Hasil pengurangan: {number1} - {number2} = {subtraction}")
print(f"Hasil perkalian: {number1} * {number2} = {multiplication}")
print(f"Hasil sisa bagi: {number1} % {number2} = {modulus}")
print(f"{number1} adalah bilangan {is_odd_or_even(number1)}")
print(f"{number2} adalah bilangan {is_odd_or_even(number2)}")