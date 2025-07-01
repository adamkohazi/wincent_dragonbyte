import os

# Function to find that number divisible by 9 or not
def is_div_by_nine(n):
    # Compute sum of digits
    sum_mod_nine = 0
    for digit in str(n):
        sum_mod_nine = (sum_mod_nine + int(digit)) % 9
    
    # Check if sum of digits is divisible by 9.
    return sum_mod_nine == 0

# Function to calculate the digit sum of a number
def digit_sum(n):
    return sum(int(d) for d in str(n))

def generate_numbers_with_digit_sum(target_sum, d):
    seen = set()
    def backtrack(current, length, digit_sum, max_length):
        if length == max_length:
            if digit_sum == target_sum:
                num = int(current)
                # Check if num + d or num - d exists in seen set
                if (num + d) in seen:
                    return (num, num + d)
                if (num - d) in seen:
                    return (num - d, num)
                seen.add(num)
            return None

        for digit in range(10):
            if length == 0 and digit == 0:
                continue  # Skip leading zero
            if digit_sum + digit <= target_sum:
                res = backtrack(current + str(digit), length + 1, digit_sum + digit, max_length)
                if res is not None:
                    return res
        return None

    for digits in range(1, 19):
        result = backtrack("", 0, 0, digits)
        if result is not None:
            return result

    return None


# Function to find two numbers with the same digit sum and a difference of d
def find_pair_with_same_digit_sum(d):
    # If the sum of digits are the same, difference is always divisible by 9
    if not is_div_by_nine(d):
        return None
    
    # Let s be sum of digits
    for s in range(1, 163): #(maximum digit sum for 18-digit number: 9*18)
        numbers = generate_numbers_with_digit_sum(s, d)
        if numbers is not None:
            return numbers

    raise ValueError('Unexpected end of code.')

# Read input values
current_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_folder, 'input_files')

# List all files in the input_files directory
input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

# Process each file
for input_file in input_files:
    # Read input file and printing to console
    input_path = os.path.join(input_folder, input_file)
    with open(input_path, 'r') as in_file:
        print('-- Reading input file: ', input_file, '--')
        content = in_file.read()
        lines = content.splitlines()

    # Processing input file content
    # First line contains the number of test cases
    t = int(lines[0].strip())
    # The next t lines contain the values of d
    test_cases = [int(line.strip()) for line in lines[1:t+1]]

    # Process each test case
    results = []
    for i, d in enumerate(test_cases):
        print(f'case {i+1}/{t}: Difference = {d})')
        result = find_pair_with_same_digit_sum(d)
        
        if result:
            results.append(f"{result[0]} {result[1]}")
            print(f'Solution: {result})')
        else:
            results.append("NONE")
            print('Unsolvable')

    # Create output filename by replacing .in with .out
    output_folder = os.path.join(current_folder, 'solutions')
    output_file = os.path.splitext(input_file)[0] + '.out'
    output_path = os.path.join(output_folder, output_file)
    # Write the results to the output file
    with open(output_path, 'w') as out_file:
        print('-- Writing output file: ', output_file, '--')
        for line in results:
            out_file.write(line + '\n')
            print(line)
