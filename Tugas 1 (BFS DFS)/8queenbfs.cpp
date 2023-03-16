#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 8

// Define a struct to represent a Queen, which has a row and column position
typedef struct {
    int row, col;
} Queen;

// Define a struct to represent a Node, which contains an array of Queens and a level indicating how many Queens are currently in the array
typedef struct {
    Queen queens[N];
    int level;
} Node;

// A function to check if a given Queen is safe to place on the board, given an array of other Queens already placed
bool isSafe(Queen queen, Queen queens[], int numQueens) {
    for (int i = 0; i < numQueens; i++) {
        if (queen.row == queens[i].row || queen.col == queens[i].col || 
            abs(queen.row - queens[i].row) == abs(queen.col - queens[i].col)) {
            // The new Queen is in the same row or column or diagonal as another Queen, so it's not safe
            return false;
        }
    }
    // The new Queen is safe to place
    return true;
}

// A function to perform a breadth-first search to find a solution to the N-Queens problem
void bfs() {
    // Initialize a queue to hold the Nodes that we need to explore
    Node queue[100000];
    int front = -1, rear = -1;
    // Initialize the first Node in the queue with an empty array of Queens and a level of 0
    Node node = { .level = 0 };
    queue[++rear] = node;

    // Keep exploring Nodes in the queue until we find a solution or the queue is empty
    while (front != rear) {
        // Remove the first Node from the queue and explore it
        node = queue[++front];
        // If the Node has N Queens, we have found a solution!
        if (node.level == N) {
            printf("Solution found:\n");
            for (int i = 0; i < N; i++) {
                printf("(%d,%d) ", node.queens[i].row, node.queens[i].col);
            }
            printf("\n");
            return;
        }
        // Try adding a Queen to each column in the next row of the board
        for (int col = 0; col < N; col++) {
            Queen queen = {node.level, col};
            // Check if the new Queen is safe to place
            if (isSafe(queen, node.queens, node.level)) {
                // If it is safe, create a new Node with the new Queen added to the array, and add it to the queue
                Node newNode = node;
                newNode.queens[newNode.level] = queen;
                newNode.level++;
                queue[++rear] = newNode;
            }
        }
    }
    // If we have explored all possible Nodes and haven't found a solution, there is no solution
    printf("Solution not found.\n");
}

// The main function just calls the bfs function and returns 0
int main() {
    bfs();
    return 0;
}
