/*BINARY INSERTION SORT: Chèn nhị phân trực tiếp trên 1 dãy ban đầu không có thứ tự
Cải tiến hơn Insertion Sort là thay vì dùng duyệt tuyến tính, dùng tìm nhị phân để xác định nhanh hơn -> Time Complexity reduces: O(log10(N))
Space Complexity: O(1)
Idea:
    1. Start at the 2nd element, because the 1st is assumed sorted
    2. Using Binary Search to find the correct index in the sorted part of the array for the current value
    3. Calculate the middle element of that sub array and compare to the current value
    4. Keep narrow it down till it is smaller than the middle element
    5. Continue until the array is sorted
*/


// INCLUDE LIBRARY
#include <bits/stdc++.h>
using namespace std;

// SORT FUNCTION for int
void binary_insertion_sort_int(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int x = a[i], left = 0, right = i - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (x > a[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        for (int j = i - 1; j >= left; j--) {
            a[j + 1] = a[j];
        }

        a[left] = x;

        // Print the array after each pass
        cout << "Array after pass " << i << ": ";
        for (int k = 0; k < n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

// SORT FUNCTION for double
void binary_insertion_sort_double(double a[], int n) {
    for (int i = 1; i < n; i++) {
        double x = a[i], left = 0, right = i - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (x > a[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        for (int j = i - 1; j >= left; j--) {
            a[j + 1] = a[j];
        }

        a[left] = x;

        // Print the array after each pass
        cout << "Array after pass " << i << ": ";
        for (int k = 0; k < n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
    }
}

// Function to generate a large test array of integers
void generate_large_test_array(int a[], int size) {
    iota(a, a + size, 1); // Fill the array with values from 1 to size
    random_shuffle(a, a + size);
}

// DRIVER FUNCTION
int main() {
    // Test with int array
    int n;
    cout << "Enter the number of elements (int): ";
    cin >> n;
    int a[n];
    cout << "The original array: ";
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Call the function to sort the original array
    binary_insertion_sort_int(a, n);

    // Print out the sorted array
    cout << "The array after being sorted: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] << " ";
    }
    cout << endl;

    // Generate a large test array
    int test_size = 10000000;
    int* test_array = new int[test_size];
    generate_large_test_array(test_array, test_size);

    // Measure time for binary insertion sort
    clock_t start = clock();
    binary_insertion_sort_int(test_array, test_size);
    clock_t end = clock();
    cout << "Binary Insertion Sort time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Generate another large test array
    generate_large_test_array(test_array, test_size);

    // Measure time for std::sort
    start = clock();
    sort(test_array, test_array + test_size);
    end = clock();
    cout << "std::sort time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Cleanup
    delete[] test_array;

    return 0;
}

