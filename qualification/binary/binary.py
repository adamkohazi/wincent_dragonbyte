import os

# For debugging
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

# Check if n in the given base contains only digits 0 and 1.
def is_binary(n, base):
    while n > 0:
        digit = n % base
        if digit > 1:
            return False
        n //= base
    return True

def nth_root(x, n):
    root = x ** (1 / n)
    rounded = round(root)
    return rounded if rounded ** n == x else root

def smallest_binary_base(n):
    # Special cases for small numbers
    if n < 3:
        return -1
    if n == 3:
        return 3
    # Assume worst-case, base n-1 representation is always 11
    # Try to reduce by checking bases where a new digit appears in the representation
    lowest = n - 1
    i = 2
    # If we go below base 3, return the current best base
    while (base := int(nth_root(n, i))) >= 3:
        if is_binary(n, base):
            lowest = base
        # Go to next suspect   
        i += 1
    return lowest
    
# Read input values
current_folder = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_folder, 'input_files')

# List all files in the input_files directory
input_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

for input_file in input_files:
    # Read input file and printing to console
    input_path = os.path.join(input_folder, input_file)
    with open(input_path, 'r') as in_file:
        print('Reading input file: ', input_file)
        content = in_file.read()
        lines = content.splitlines()

    # Processing input file content
    t = int(lines[0].strip()) # Number of test cases
    test_cases = [int(line.strip()) for line in lines[1:t+1]]

    # Execute logic
    results = []
    for i, n in enumerate(test_cases):
        print(f'{i}/{t}) input: {n}')
        result = smallest_binary_base(n)
        if result > 0:
            representation = ''.join([str(d) for d in numberToBase(n, result)])
        else:
            representation = result
        print(f'result: base {result} - {representation}')
        results.append(str(result))

    # Create output filename by replacing .in with .out
    output_folder = os.path.join(current_folder, 'solutions')
    output_file = os.path.splitext(input_file)[0] + '.out'
    output_path = os.path.join(output_folder, output_file)

    # Write the results to the output file
    with open(output_path, 'w') as out_file:
        print('Writing output file: ', output_file)
        out_file.write('\n'.join(results))