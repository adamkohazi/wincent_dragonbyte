import os

MAXDIGITS = 6
MAXNUMBER = 10**MAXDIGITS

# Function to calculate the digit sum of a number
def digit_sum(n):
    return sum(int(d) for d in str(n))

# Function to find two numbers with the same digit sum and a difference of d
def find_pair_with_same_digit_sum(d):
    for a in range(1, 10**6):  # Search up to a reasonable upper bound
        b = a + d
        if digit_sum(a) == digit_sum(b):
            return a, b
    return None  # Return None if no such pair is found

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
        print(content)
        lines = content.splitlines()

    # Processing input file content
    # First line contains the number of test cases
    t = int(lines[0].strip())
    # The next t lines contain the values of d
    test_cases = [int(line.strip()) for line in lines[1:t+1]]

    # Process each test case
    results = []
    for d in test_cases:
        result = find_pair_with_same_digit_sum(d)
        if result:
            results.append(f"{result[0]} {result[1]}")
        else:
            results.append("NONE")

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
