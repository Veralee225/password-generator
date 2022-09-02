#!/usr/bin/python3

"""
The random is a python module that generates random numbers
"""

import random

print("Password Generator")

# Character contains all the characters needed to generate the password.
characters = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?#0123456789")

number = input("How many passwords do you want to generate?: ")
number = int(number)

# Length helps you select the length of your password

length = input("Input the length of your password: ")
length = int(length)

print("\nhere are your passwords: ")

# A simple for loop function that helps the user get the password
for password in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(characters)
    print(passwords)
