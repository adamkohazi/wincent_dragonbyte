import os
import math

# Greedy move generator
def generate_moves(test_case):
    x, y = 0, 0  # starting position
    time = 0
    weight = test_case['w']
    objects = test_case['objects'].copy()
    moves = []

    while True:
        # Find all assimilable objects
        candidates = [
            (math.dist((x, y), (ox, oy)), id, ox, oy, oz)
            for (id, ox, oy, oz) in objects
            if weight > 2 * oz
        ]

        if not candidates:
            break  # no more objects can be assimilated

        # Choose nearest assimilable object
        candidates.sort()
        dist, id, ox, oy, oz = candidates[0]

        # Move to object and assimilate
        time += dist + 1
        weight += oz
        x, y = ox, oy
        objects.remove((id, ox, oy, oz))

        moves.append((round(time, 6), weight, id, (ox, oy, oz)))

    return moves

    
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
    index = 1  # Current line index
    test_cases = []

    for case in range(t):
        n, w = map(int, lines[index].split())
        index += 1
        objects = []
        for i in range(n):
            x, y, z = map(int, lines[index].split())
            objects.append((i, x, y, z))
            index += 1
        test_cases.append({
            'n': n,
            'w': w,
            'objects': objects
        })

    # Execute logic
    results = []
    for i, case in enumerate(test_cases):
        print(f'case {i+1}/{t})')
        
        moves = generate_moves(case)
        for move in moves:
            print(f"Time: {move[0]}, New weight: {move[1]}, Object {move[2]} assimilated at: {move[3]}")
        results.append(str(len(moves)))
        results.append(' '.join(str(move[2]) for move in moves))  

    # Create output filename by replacing .in with .out
    output_folder = os.path.join(current_folder, 'solutions')
    output_file = os.path.splitext(input_file)[0] + '.out'
    output_path = os.path.join(output_folder, output_file)

    # Write the results to the output file
    with open(output_path, 'w') as out_file:
        print('Writing output file: ', output_file)
        out_file.write('\n'.join(results))
        print(results)