#include <iostream>
using namespace std;

int main()
{
    int rowIndex, glassIndex, currentRow;
    double overflow;
    float pouredAmount;

    // Welcome message
    cout << "Welcome to the Champagne Tower Simulator!" << endl;
    cout << "Enter the total poured amount of champagne (e.g., 1.5): ";
    cin >> pouredAmount;

    // Input for row
    cout << "Enter the row number you want to check: ";
    cin >> rowIndex;

    // Input for glass in that row with validation
    while (true) {
        cout << "Enter the glass number in that row: ";
        cin >> glassIndex;
        if (glassIndex >= 1 && glassIndex <= rowIndex) {
            break; // valid input
        } else {
            cout << "Invalid glass number. It must be between 1 and " << rowIndex << ". Please try again." << endl;
        }
    }

    // Initialize tower
    float tower[100][100] = {};
    if (pouredAmount > 1) tower[1][1] = pouredAmount;

    // Fill the tower
    for (currentRow = 1; currentRow <= rowIndex; currentRow++) {
        for (int glassInRow = 1; glassInRow <= currentRow; glassInRow++) {
            // Calculate overflow
            overflow = (tower[currentRow][glassInRow] - 1) / 2;
            if (overflow < 0) overflow = 0; // no negative overflow

            // Spread overflow to next row
            tower[currentRow + 1][glassInRow] += overflow;
            tower[currentRow + 1][glassInRow + 1] += overflow;

            // Cap the current glass to max 1 and min 0
            if (tower[currentRow][glassInRow] > 1) tower[currentRow][glassInRow] = 1;
            if (tower[currentRow][glassInRow] < 0) tower[currentRow][glassInRow] = 0;

            // Check if this is the requested glass
            if (currentRow == rowIndex && glassInRow == glassIndex) {
                cout << "Amount in the glass: ";
                cout << fixed;
                cout.precision(3);
                cout << tower[currentRow][glassInRow] << " liters" << endl;
                break;
            }
        }
        if (currentRow == rowIndex) break;
    }

    // Keep .exe window open
    cout << "Press Enter to exit...";
    cin.ignore();
    cin.get();

    return 0;
}
