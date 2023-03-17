import numpy as np

# Fungsi untuk menghitung Manhattan Distance
def manhattan_distance(state, target):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = np.where(target == state[i][j])
                distance += abs(i - x[0]) + abs(j - y[0])
    return distance

# Fungsi untuk mencari gerakan selanjutnya
def next_move(state, target):
    moves = []
    blank_row, blank_col = np.where(state == 0)
    row, col = blank_row[0], blank_col[0]
    
    # Cek apakah bisa geser ke atas
    if row > 0:
        new_state = state.copy()
        new_state[row][col], new_state[row-1][col] = new_state[row-1][col], new_state[row][col]
        distance = manhattan_distance(new_state, target)
        moves.append(('UP', new_state, distance))
        
    # Cek apakah bisa geser ke bawah
    if row < 2:
        new_state = state.copy()
        new_state[row][col], new_state[row+1][col] = new_state[row+1][col], new_state[row][col]
        distance = manhattan_distance(new_state, target)
        moves.append(('DOWN', new_state, distance))
        
    # Cek apakah bisa geser ke kiri
    if col > 0:
        new_state = state.copy()
        new_state[row][col], new_state[row][col-1] = new_state[row][col-1], new_state[row][col]
        distance = manhattan_distance(new_state, target)
        moves.append(('LEFT', new_state, distance))
        
    # Cek apakah bisa geser ke kanan
    if col < 2:
        new_state = state.copy()
        new_state[row][col], new_state[row][col+1] = new_state[row][col+1], new_state[row][col]
        distance = manhattan_distance(new_state, target)
        moves.append(('RIGHT', new_state, distance))
        
    # Urutkan gerakan berdasarkan jarak terpendek
    moves.sort(key=lambda x: x[2])
    return moves[0]

# Fungsi untuk menyelesaikan puzzle
def solve_puzzle(initial_state, target_state):
    state = initial_state.copy()
    moves = []
    while not np.array_equal(state, target_state):
        move, state, _ = next_move(state, target_state)
        print(state)
        moves.append(move)
    return moves

# Contoh penggunaan program
initial_state = np.array([[0, 2, 3], [1, 5, 6], [4, 7, 8]])
target_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
print(initial_state)
moves = solve_puzzle(initial_state, target_state)
print(moves)
