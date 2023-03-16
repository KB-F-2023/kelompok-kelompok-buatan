from random import randint

# Set the number of queens and board size
N = 8

# Define a function to randomly place queens on the board
def configure_randomly():
    state = [randint(0, N-1) for i in range(N)]
    return state

# Define a function to calculate the number of queens attacking each other
def calculate_attacking_queens(state):
    attacking = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i]-state[j]) == abs(i-j):
                attacking += 1
    return attacking

# Define a function to find the best state (with the fewest attacking queens)
def find_best_state():
    state = configure_randomly()
    attacking = calculate_attacking_queens(state)
    while True:
        if attacking == 0:
            return state
        new_state = configure_randomly()
        new_attacking = calculate_attacking_queens(new_state)
        if new_attacking < attacking:
            state = new_state
            attacking = new_attacking
            if attacking == 0:
                return state
        elif new_attacking == attacking:
            state = new_state if randint(0, 1) == 0 else state

# Run the algorithm and print the result
result = find_best_state()
print(result)

# Turn result to its matrix representation
for i in range(N):
    for j in range(N):
        if result[i] == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()