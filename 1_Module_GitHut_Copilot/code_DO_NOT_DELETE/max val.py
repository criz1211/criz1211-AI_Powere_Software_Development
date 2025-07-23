# project/max val.py
# This script defines a function to find the maximum value in a list of numbers.
# It also includes an example usage of the function.

def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

if __name__ == "__main__":
    data = input("Enter numbers separated by spaces: ")
    nums = [float(x) for x in data.split()]
    print("Maximum value:", find_max(nums))

