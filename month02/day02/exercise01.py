#!usr/bin/python3
import os
result = 1
for number in range(100):
    if number % 2:
        result *= number

print(result)

