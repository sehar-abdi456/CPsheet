n = int(input())  # Read input number
digits = str(n)   # Convert number to string
new_number_str = ""  # Initialize an empty string

for i, digit in enumerate(digits):  # Iterate over each digit with index
    digit_int = int(digit)  # Convert character to integer
    if digit_int >= 5:
        add = 9 - digit_int  # Transform the digit
        # Prevent leading zero in the final number
        if i == 0 and add == 0:
            new_number_str += digit  # Keep the original first digit
        else:
            new_number_str += str(add)  # Append transformed digit
    else:
        new_number_str += digit  # Append unchanged digit

# Convert the modified string back to an integer
new_number = int(new_number_str)
print(new_number)  # Output the result


