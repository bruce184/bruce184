/*SELECTION SORT: Chọn Trực Tiếp trên danh sách ban đầu không có thứ tự
Time Complexity: O(n^2) because there is nested loop
Space Complexity: O(1)
Idea:
    1. Set the current value to be the smallest
    2. Compare it to the next one
    3. If it is greater than the next one <-> the next one is SMALLER -> SWAP THEM
    4. Repeat until the array is sorted
*/


// INCLUDE LIBRARY
#include <bits/stdc++.h>
using namespace std;

// SORT FUNCTION for int
void selection_sort_int(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[min_idx], a[i]);

}
}

// SORT FUNCTION for double
void selection_sort_double(double a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[min_idx], a[i]);

        // Print the array after each pass
        cout << "Array after pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

// Function to check if array is sorted for int
bool is_sorted_int(int a[], int n) {
    for (int i = 1; i < n; i++) {
        if (a[i - 1] > a[i]) {
            return false;
        }
    }
    return true;
}

// Function to check if array is sorted for double
bool is_sorted_double(double a[], int n) {
    for (int i = 1; i < n; i++) {
        if (a[i - 1] > a[i]) {
            return false;
        }
    }
    return true;
}

// Function to generate a large test array of integers
void generate_large_test_array(int a[], int size) {
    iota(a, a + size, 1);
    random_shuffle(a, a + size);
}

// DRIVER FUNCTION
int main(){
    // Test with int array
    int n;
    cout << "Enter the number of elements (int): ";
    cin >> n;
    int a[n];
    cout << "The original array: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }


    // Call the function to sort the original array of integers
    selection_sort_int(a, n);

    // Print out the sorted array
    cout << "The array after being sorted: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    // Check if the array is sorted correctly
    if (is_sorted_int(a, n)) {
        cout << "Selection Sort result is correct!" << endl;
    } else {
        cout << "Selection Sort result is incorrect!" << endl;
    }

    // sort(a, a + n);


    return 0;
}

