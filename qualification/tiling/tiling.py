import os

# Helper function for figuring out patterns
def find_min_cost(w, h):
    points = ((w+1)//2) * ((h+1)//2)
    # Lets assume every point is covered with a tetromino
    # We'll need to replace this many of those, in order to fit into the area (note: this doesn't guarantee a valid tiling)
    return (4 * points) - w * h

def find_tiling(w, h):
    # If it can't be tiled with triminos, there's no chance:
    if ((((w+1)//2) * ((h+1)//2)) * 3) > (w*h):
        return None

    # If both dimensions are even, checkerboard pattern is optimal
    if w % 2 == 0 and h % 2 == 0:
        tiling = ''
        for y in range(h):
            row = ''
            for x in range(w):
                if ((x//2) + (y//2)) % 2 == 0:
                    row += 'a'
                else:
                    row += 'b'
            tiling += row
            if y < w-1:
                tiling += '\n'
        return tiling
    
    # Minimum cost tiling for 7x7
    if w==7 and h==7:
        return '''aabbabb
aabaaba
bbddcaa
bacdccb
aaccdbb
bbabdda
baabbaa'''
    
    # From here on, there's a pattern:
    if w==h:
        tiling = ''
        for y in range(h):
            if y==0:
                tiling += 'aabbabb'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'd'
                    else:
                        tiling += 'b'
            elif y==1:
                tiling += 'aabaaba'
                for x in range(7,w):
                    if   (x-7) % 4 == 0:
                        tiling += 'd'
                    elif (x-7) % 4 == 1:
                        tiling += 'c'
                    elif (x-7) % 4 == 2:
                        tiling += 'b'
                    else:
                        tiling += 'a'
            elif y==2:
                tiling += 'bbddcaa'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'c'
                    else:
                        tiling += 'a'
            elif y==3:
                tiling += 'bacdccb'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'd'
                    else:
                        tiling += 'b'
            elif y==4:
                tiling += 'aaccdbb'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'd'
                    else:
                        tiling += 'b'
            elif y==5:
                tiling += 'bbabdda'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'c'
                    else:
                        tiling += 'a'
            elif y==6:
                tiling += 'baabbaa'
                for x in range(7,w):
                    if ((x-7)//2) % 2 == 0:
                        tiling += 'c'
                    else:
                        tiling += 'a'

            elif (y-7) % 4 == 0:
                tiling += 'ddc'
                for x in range(3,w):
                    if ((x-3)//2) % 2 == 0:
                        tiling += 'd'
                    else:
                        tiling += 'c'
            elif (y-7) % 4 == 1:
                tiling += 'd'
                for x in range(1,w):
                    if ((x-1)//2) % 2 == 0:
                        tiling += 'c'
                    else:
                        tiling += 'd'
            elif (y-7) % 4 == 2:
                tiling += 'bba'
                for x in range(3,w):
                    if ((x-3)//2) % 2 == 0:
                        tiling += 'b'
                    else:
                        tiling += 'a'
            elif (y-7) % 4 == 3:
                tiling += 'b'
                for x in range(1,w):
                    if ((x-1)//2) % 2 == 0:
                        tiling += 'a'
                    else:
                        tiling += 'b'
            if y < w-1:
                tiling += '\n'
        return tiling
    print('error?')

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
    for n in test_cases:
        result = find_tiling(n, n)
        if result:
            results.append('YES\n' + result)
        else:
            results.append('NO')

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