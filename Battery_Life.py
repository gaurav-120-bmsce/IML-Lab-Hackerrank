def calculate_value(number):
    if number < 4:
        return(number * 2)
    else:
        return(8)

input_number = float(input())
print(calculate_value(input_number))
