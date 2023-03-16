#include <bits/stdc++.h>
using namespace std;

// A set to keep track of visited states
set<string> vis;

// A function to get the position of an adjacent tile given the current position of the blank tile
int getPos(int idx, int dest) {
    int row = idx / 3;
    int col = idx % 3;
    if(dest == 0)
        return (col == 0 ? -1 : 3 * row + col - 1); // move left
    else if(dest == 1)
        return (col == 2 ? -1 : 3 * row + col + 1); // move right
    else if(dest == 2)
        return (row == 0 ? -1 : 3 * (row - 1) + col); // move up
    else
        return (row == 2 ? -1 : 3 * (row + 1) + col); // move down
}

// The BFS function to solve the 8-puzzle problem
void bfs(string start, string finish) {
    // A queue to store the states that need to be expanded
    queue<pair<string, int>> q;
    // Initialize the queue with the starting state and a step count of 0
    q.push(make_pair(start, 0));
    while(!q.empty()) {
        // Dequeue the front element of the queue and store its state and step count
        string cur = q.front().first;
        int step = q.front().second;

        // Print the current state and step count for visualization
        cout << "Step " << step << endl;
        for(int i = 0; i < 9; ++i){
            cout << cur[i] << " ";
            if((i + 1) % 3 == 0)
                cout << endl;
        }
        cout << endl;
        
        // Mark the current state as visited
        if(!vis.count(cur))
            vis.insert(cur);
        q.pop();

        // Check if the goal state has been reached
        if(cur == finish){
            cout << "Total steps: " << step << endl;
            return;
        }

        // Find the position of the blank tile in the current state
        int blankPos = -1;
        for(int i = 0; i < 9; ++i) {
            if(cur[i] == '0') {
                blankPos = i;
                break;
            }
        }

        // Generate the child states by swapping the blank tile with its adjacent tiles
        for(int i = 0; i < 4; ++i) {
            int nextPos = getPos(blankPos, i);
            if(nextPos != -1) {
                string nextStr = cur;
                swap(nextStr[blankPos], nextStr[nextPos]);

                // Add the child state to the queue if it has not been visited before
                if(!vis.count(nextStr)) {
                    vis.insert(nextStr);
                    q.push(make_pair(nextStr, step + 1));
                }
            }
        }
    }   
}

// The main function to initialize the starting and goal states and call the BFS function
int main() {
    // Initialize the starting and goal states as strings
    string start = "123845760";
    string finish = "123804765";
    // Call the BFS function to solve the 8-puzzle problem
    bfs(start, finish);
    return 0;
}
