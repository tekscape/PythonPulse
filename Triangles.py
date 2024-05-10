def print_triangle(rows):
    if rows <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    for i in range(1, rows + 1):
        # Number of spaces
        spaces = rows - i
        # Number of asterisks
        asterisks = (2 * i) - 1
        # Printing spaces
        print(" " * spaces, end="")
        # Printing asterisks
        print("*" * asterisks)

def print_inverted_triangle(rows):
    if rows <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    for i in range(rows, 0, -1):
        # Number of spaces
        spaces = rows - i
        # Number of asterisks
        asterisks = (2 * i) - 1
        # Printing spaces
        print(" " * spaces, end="")
        # Printing asterisks
        print("*" * asterisks)

# Testing the functions
rows = int(input("Enter the number of rows for the triangle: "))
print("Triangle:")
print_triangle(rows)

print("\nInverted Triangle:")
print_inverted_triangle(rows)
