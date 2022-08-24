"""
Write a python script to print first N odd natural numbers
in reverse order 
"""

for i in range(int(input("Enter a natural number: ")) * 2, 0, -2):
    print(i - 1, end=" ")
