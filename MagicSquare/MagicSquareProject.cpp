#include <iostream>
using namespace std;

int main() 
{
    // Display program header
    cout << "=== Magic Square Generator ===\n";
    cout << "Enter an odd number 'n' to generate an n x n magic square.\n";
    cout << "The magic square will be displayed below.\n\n";

    int magicSquare[100][100]; // Matrix to hold the magic square
    int size, currentNumber = 1; // 'size' is n, currentNumber is the number being placed

    cout << "Enter the size of the magic square (odd number): ";
    cin >> size;

    // Initialize all cells with -2 (empty)
    for (int row = 0; row < size; row++) {
        for (int col = 0; col < size; col++) {
            magicSquare[row][col] = -2;
        }
    }

    // Fill the magic square
    for (int row = 0; row < size; row++) {
        for (int col = 0; col < size; col++) {
            magicSquare[0][size / 2] = 1; // Place the first number in the middle of the first row

            if (magicSquare[row][col] == currentNumber) {
                currentNumber++;

                // Calculate next position
                if (row - 1 == -1 && col - 1 >= 0) {
                    if (magicSquare[row - 1 + size][col - 1] == -2) {
                        magicSquare[row - 1 + size][col - 1] = currentNumber;
                        col = -1; row = 0;
                    } else {
                        magicSquare[row + 1][col] = currentNumber;
                        col = -1; row = 0;
                    }
                } 
                else if (row - 1 >= 0 && col - 1 == -1) {
                    if (magicSquare[row - 1][col - 1 + size] == -2) {
                        magicSquare[row - 1][col - 1 + size] = currentNumber;
                        col = -1; row = 0;
                    } else {
                        magicSquare[row + 1][col] = currentNumber;
                        col = -1; row = 0;
                    }
                } 
                else if (row - 1 == -1 && col - 1 == -1) {
                    if (magicSquare[row - 1 + size][col - 1 + size] == -2) {
                        magicSquare[row - 1 + size][col - 1 + size] = currentNumber;
                        col = -1; row = 0;
                    } else {
                        magicSquare[row + 1][col] = currentNumber;
                        col = -1; row = 0;
                    }
                } 
                else if (row - 1 >= 0 && col - 1 >= 0) {
                    if (magicSquare[row - 1][col - 1] == -2) {
                        magicSquare[row - 1][col - 1] = currentNumber;
                        col = -1; row = 0;
                    } else {
                        magicSquare[row + 1][col] = currentNumber;
                        col = -1; row = 0;
                    }
                }
            }

            // Stop filling if all numbers are placed
            if (currentNumber == size * size) {
                break;
            }
        }
        if (currentNumber == size * size) {
            break;
        }
    }

    // Print the magic square
    cout << "\nMagic Square of size " << size << " x " << size << ":\n";
    for (int row = 0; row < size; row++) {
        for (int col = 0; col < size; col++) {
            cout << magicSquare[row][col] << "\t";
        }
        cout << endl;
    }

    // Keep the console open
    cout << "\nPress Enter to exit...";
    cin.ignore(); // Ignore leftover newline from previous input
    cin.get();    // Wait for Enter key

    return 0;
}
