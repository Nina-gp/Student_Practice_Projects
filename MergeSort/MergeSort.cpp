#include <iostream>
using namespace std;

// Merge function to merge two halves of the array
void merge(int arr[], int left, int mid, int right, int size)
{
    int i = left;       // Starting index of left subarray
    int j = mid + 1;    // Starting index of right subarray
    int k = left;       // Index for temporary array

    int temp[size];     // Temporary array

    // Merge the two subarrays into temp[]
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            temp[k++] = arr[i++];
        }
        else {
            temp[k++] = arr[j++];
        }
    }

    // Copy remaining elements of left subarray, if any
    while (i <= mid) temp[k++] = arr[i++];

    // Copy remaining elements of right subarray, if any
    while (j <= right) temp[k++] = arr[j++];

    // Copy merged elements back to original array
    for (int p = left; p <= right; p++) arr[p] = temp[p];
}

// MergeSort function: recursively sorts array
void mergeSort(int arr[], int left, int right, int size)
{
    if (left < right) {
        int mid = (left + right) / 2;

        mergeSort(arr, left, mid, size);      // Sort first half
        mergeSort(arr, mid + 1, right, size); // Sort second half
        merge(arr, left, mid, right, size);   // Merge sorted halves
    }
}

int main()
{
    cout << "Welcome to your Merge Sort program!" << endl;
    cout << "Enter the number of integers you want to sort: ";
    int size;
    cin >> size;

    int numbers[size]; // Array to store the integers

    cout << "Enter " << size << " integers separated by spaces: " << endl;
    for (int i = 0; i < size; i++) {
        cin >> numbers[i];
    }

    cout << "\nNumbers before sorting: ";
    for (int i = 0; i < size; i++) cout << numbers[i] << " ";
    cout << endl;

    mergeSort(numbers, 0, size - 1, size); // Call mergesort

    cout << "Numbers after sorting: ";
    for (int i = 0; i < size; i++) cout << numbers[i] << " ";
    cout << endl;

    cout << "\nSorting completed. Press Enter to exit." << endl;
    cin.ignore(); // Ignore leftover newline from previous input
    cin.get();    // Wait for user to press Enter

    return 0;
}
