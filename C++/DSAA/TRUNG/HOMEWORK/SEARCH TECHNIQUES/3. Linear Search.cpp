// INCLUDE LIBRARIES
#include <bits/stdc++.h>
using namespace std;

// SEARCH FUNCTION for int
int linear_search_int(int a[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            return i;
        }
    }
    return -1;
}

// SEARCH FUNCTION for double
int linear_search_double(double a[], int n, double x) {
    for (int i = 0; i < n; i++) {
        if (a[i] == x) {
            return i;
        }
    }
    return -1;
}

// Function to generate a large test array of integers
void generate_large_test_array(int a[], int size) {
    iota(a, a + size, 1); // Fill the array with values from 1 to size
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

    // Ask for the number to search
    cout << "What number you want to find in the array: ";
    int x;
    cin >> x;

    // Call the function to search
    int res = linear_search_int(a, n, x);
    if (res != -1) {
        cout << x << " is at index " << res << " of the array." << endl;
    } else {
        cout << x << " is not found in the array." << endl;
    }

    // Generate a large test array
    int test_size = 10000000;
    int* test_array = new int[test_size];
    generate_large_test_array(test_array, test_size);

    // Measure time for linear search
    int search_value = test_size / 2; // Search for the middle value
    clock_t start = clock();
    int search_result = linear_search_int(test_array, test_size, search_value);
    clock_t end = clock();
    cout << "Linear Search time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Measure time for std::find
    start = clock();
    auto std_search_result = find(test_array, test_array + test_size, search_value);
    end = clock();
    cout << "std::find time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Cleanup
    delete[] test_array;

    return 0;
}
