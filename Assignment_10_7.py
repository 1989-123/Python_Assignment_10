"""
Write a python script to print first N even natural numbers
in reverse order 
"""

for i in range(int(input("Enter a natural number: ")) * 2, 1, -2):
    print(i, end=" ")
