import os

def print_case(case):
    d = case['d']
    rooks = case['rooks']

    # Initialize an empty board with '.' for empty cells
    board = [['.' for _ in range(d)] for _ in range(d)]

    # Place rooks
    for r, c, t in rooks:
        board[r][c] = t  # t is either 'W' or 'B'

    # Print board
    for row in board:
        print(''.join(row))
    print('')

def print_moves(moves):
    for move in moves:
        start, end = move
        print(f"From ({start[0]}, {start[1]}) to ({end[0]}, {end[1]})")

def generate_moves(case, color):
    d = case['d']
    rooks = case['rooks']
    
    # Build board
    board = [['.' for _ in range(d)] for _ in range(d)]
    rook_positions = []

    for r, c, t in rooks:
        board[r][c] = t
        if t == color:
            rook_positions.append((r, c))

    moves = []  # Each move is ((from_row, from_col), (to_row, to_col), capture)
    enemy_color = 'B' if color == 'W' else 'W'

    for index, (r, c) in enumerate(rook_positions):
        # Move Up
        for i in range(r - 1, -1, -1):
            if board[i][c] == '.':
                moves.append(((r, c), (i, c)))
            elif board[i][c] == enemy_color:
                moves.append(((r, c), (i, c)))
                break
            else:  # Own color
                break

        # Move Down
        for i in range(r + 1, d):
            if board[i][c] == '.':
                moves.append(((r, c), (i, c)))
            elif board[i][c] == enemy_color:
                moves.append(((r, c), (i, c)))
                break
            else:
                break

        # Move Left
        for j in range(c - 1, -1, -1):
            if board[r][j] == '.':
                moves.append(((r, c), (r, j)))
            elif board[r][j] == enemy_color:
                moves.append(((r, c), (r, j)))
                break
            else:
                break

        # Move Right
        for j in range(c + 1, d):
            if board[r][j] == '.':
                moves.append(((r, c), (r, j)))
            elif board[r][j] == enemy_color:
                moves.append(((r, c), (r, j)))
                break
            else:
                break

    return moves

def apply_move(case, move):
    from_pos, to_pos = move
    from_r, from_c = from_pos
    to_r, to_c = to_pos

    new_rooks = []

    moved_rook_type = None

    for r, c, t in case['rooks']:
        if (r, c) == from_pos:
            moved_rook_type = t  # Save type of moving rook
            continue  # Remove it from original position
        elif (r, c) == to_pos:
            continue  # Captured rook (if any)
        else:
            new_rooks.append((r, c, t))

    # Add moved rook to destination
    new_rooks.append((to_r, to_c, moved_rook_type))

    return {
        'd': case['d'],
        'n': len(new_rooks),
        'rooks': new_rooks
    }

    
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
        d, n = map(int, lines[index].split())
        index += 1
        rooks = []

        for _ in range(n):
            ri_ci_ti = lines[index].split()
            ri = int(ri_ci_ti[0])
            ci = int(ri_ci_ti[1])
            ti = ri_ci_ti[2]
            rooks.append((ri, ci, ti))
            index += 1

        test_cases.append({
            'd': d,
            'n': n,
            'rooks': rooks
        })

    # Execute logic
    results = []
    for i, case in enumerate(test_cases):
        print(f'case {i+1}/{t})')
        #print_case(case)
        total = 0
        white_moves = generate_moves(case, 'W')
        #print_moves(white_moves)
        for wm in white_moves:
            new_case = apply_move(case, wm)
            #print_case(new_case)
            black_moves = generate_moves(new_case, 'B')
            total += len(black_moves)
        
        # Modulo
        total = total % ((10**9) + 7)
        print(total)
        results.append(str(total))

    # Create output filename by replacing .in with .out
    output_folder = os.path.join(current_folder, 'solutions')
    output_file = os.path.splitext(input_file)[0] + '.out'
    output_path = os.path.join(output_folder, output_file)

    # Write the results to the output file
    with open(output_path, 'w') as out_file:
        print('Writing output file: ', output_file)
        out_file.write('\n'.join(results))