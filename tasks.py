# 1) 
# Create a function which converts lenght, mass, time units from SI system to CGS. 
# All arguments must hold default values if not provided.

# CGS system: the unit of Mass is Gram, the unit of Length is Centimeter, and the unit of Time is Seconds.
# Meter -> Centimeter, Kilogram -> Gram, Second -> Second 


# def convert_units_si_cgs(lenght: float = 100.0, mass: float = 50.0, time: float = 60.0) -> tuple[float]:
#     lenght_cgs: float = lenght * 100
#     mass_cgs: float = mass * 1000
#     time_cgs: float = time
#     return lenght_cgs, mass_cgs, time_cgs

# print(convert_units_si_cgs())

# 2) 
# Create a program which takes 5 random number per 1 input. 
# The create a function which takes the sum of those numbers 
# (lets agree argument is being called 'num_sum'), 
# and all those 5 numbers as separate free arguments as well. 
# Multiply all those numbers with with the num_sum you calculated in a list data structure.

# def sum_five_numers(one: int, two, three, four, five):
#     num_sum = one + two + three + four + five
#     result = [one * num_sum, two * num_sum, three * num_sum, four * num_sum, five * num_sum]
#     return one+two+three+four+five

# def multiplay_num_sum(x):
#     return (1+2+3+4+5)*x

# user_input = input("Enter five numbers separated by commas: ")
# number_list = [int(num) for num in numbers.split(',')]

# numbers: List[int]) -> int:

def multiply_by_sum(num_sum, *numbers):                 #GPT
    result = [num * num_sum for num in numbers]
    return result

def main():
    try:
        input_str = input("Enter 5 invented numbers separated by spaces: ")
        numbers = list(map(float, input_str.split()))

        if len(numbers) != 5:
            print("Please enter exactly 5 numbers.")
        else:
            num_sum = sum(numbers)
            result = multiply_by_sum(num_sum, *numbers)
            print(f"Sum of the numbers: {num_sum}")
            print(f"Result of multiplying each number by the sum: {result}")

    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()


# 3) Create lamba functions for these caclulations: 
# - calculate circle radius 
# - calculate average speed of the car (knowing distance and time passed to drive that distance) 
# - calculate percentage of value if 5500 is equal 200%