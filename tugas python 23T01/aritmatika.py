# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the perimeter of a rectangle
def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Example usage
length = 5
width = 3

# Calculate the area and perimeter
area = rectangle_area(length, width)
perimeter = rectangle_perimeter(length, width)

# Print out the results
print(f"Luas persegi panjang: {length} x {width} = {area}")
print(f"Keliling persegi panjang: 2 x ( {length} + {width} ) = {perimeter}")