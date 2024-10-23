/*INSERTION SORT: Chèn trực tiếp trên 1 dãy ban đầu không có thứ tự
Duyệt tuyến tính
Time Complexity:
    Best: O(n)
    Average: O(n^2) when the list is randomly ordered
    Worst: O(n^2) when the list reversed
Space Complexity: O(1)
Idea:
    1. Start at the 2nd element, because the 1st is assumed sorted
    2. Compare it to the 1st one
    3. If it is smaller than the 1st one <-> the 1st one is GREATER -> SWAP THEM
    4. Repeat 1-3 until the array is sorted
*/


// INCLUDE LIBRARY
#include <bits/stdc++.h>
using namespace std;

// SORT FUNCTION for int
void insertion_sort_int(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int cur = a[i];
        int pre = i - 1;
        while (pre >= 0 && a[pre] > cur) {
            a[pre + 1] = a[pre];
            pre--;
        }
        a[pre + 1] = cur;


    }
}

// SORT FUNCTION for double
void insertion_sort_double(double a[], int n) {
    for (int i = 1; i < n; i++) {
        double cur = a[i];
        int pre = i - 1;
        while (pre >= 0 && a[pre] > cur) {
            a[pre + 1] = a[pre];
            pre--;
        }
        a[pre + 1] = cur;

        // Print the array after each pass
        cout << "Array after pass " << i << ": ";
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

// MAIN FUNCTION
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
    insertion_sort_int(a, n);

    // Print out the sorted array
    cout << "The array after being sorted: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    // Check if the array is sorted correctly
    if (is_sorted_int(a, n)) {
        cout << "Insertion Sort result is correct!" << endl;
    } else {
        cout << "Insertion Sort result is incorrect!" << endl;
    }

    // sort(a, a + n);

    return 0;
}

