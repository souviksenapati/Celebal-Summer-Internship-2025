def low_tri(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print("* " * i)
    print()


def up_tri(n):
    print("Upper Triangular Pattern:")
    for i in range(n):
        print("  " * i + "* " * (n - i))
    print()


def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))
    print()


##User Input
rows = int(input("Enter the number of rows: "))

low_tri(rows)
up_tri(rows)
pyramid(rows)
