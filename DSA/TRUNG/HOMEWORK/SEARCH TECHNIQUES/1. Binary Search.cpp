/* BINARY SEARCH: on a sorted array; like Binary Search, but check fewer elements by jumping
Time Complexity: O(log(N))
Space Complexity: O(1)
Idea:
    1. Divide the array into 2 halves and find the middle element
    2. Compare the selected element vs the middle element: if greater, left++ and the opposite
    3. Continue until found
*/


// INCLUDE LIBRARIES
#include <bits/stdc++.h>
using namespace std;

// SEARCH FUNCTION for int
int binary_search_int(int a[], int n, int x) {
    int left = 0, right = n - 1, mid;

    while (left <= right) {
        mid = left + (right - left) / 2;

        if (x == a[mid]) {
            return mid;
        } else if (x > a[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

// SEARCH FUNCTION for double
int binary_search_double(double a[], int n, double x) {
    int left = 0, right = n - 1, mid;

    while (left <= right) {
        mid = left + (right - left) / 2;

        if (x == a[mid]) {
            return mid;
        } else if (x > a[mid]) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return -1;
}

// Function to generate a sorted large test array of integers
void generate_large_sorted_test_array(int a[], int size) {
    iota(a, a + size, 1); // Fill the array with sorted values from 1 to size
}

// DRIVER FUNCTION
int main(){
    // Test with int array
    int n;
    cout << "Enter the number of elements (int): ";
    cin >> n;
    int a[n];
    cout << "The original array (must be sorted): ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Ask for the number to search
    cout << "What number you want to find in the array: ";
    int x;
    cin >> x;

    // Call the function to search
    int res = binary_search_int(a, n, x);
    if (res != -1) {
        cout << x << " is at index " << res << " of the array." << endl;
    } else {
        cout << x << " is not found in the array." << endl;
    }


    return 0;
}

