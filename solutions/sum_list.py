from typing import List

def sum_list(nums: List[int]) -> int:
    return sum(nums)

if __name__ == "__main__":
    user_input = input("Please enter a series of numbers, separated by spaces: ")
    input_parts = user_input.split()
    try:
        numbers = [int(x) for x in input_parts]
        total_sum = sum_list(numbers)
        print(f"The sum of the numbers is: {total_sum}")

    except ValueError:
        print("Invalid input. Please make sure you only enter numbers separated by spaces.")

