/* JUMP SEARCH: on a sorted array; like Binary Search, but check fewer elements by jumping
Time Complexity: O(?n)
Space Complexity: O(1)
Idea:
    1. Identify the jumping block (how many steps to jump at 1 time)
    2. Iterate on that block beginning with pre, if there's a match, display, else return -1
    3. Continue until find it

*/


// INCLUDE LIBRARIES
#include <bits/stdc++.h>
using namespace std;

// SEARCH FUNCTION for int
int jump_search_int(int a[], int n, int x) {
    int step = sqrt(n); // chia làm sao để đủ nhỏ để khi áp dụng thuật toán tìm kiếm (linear search) ko maasty thời gian
    int pre = 0;

    while (a[min(step, n) - 1] < x) {
        pre = step;
        if (pre >= n) {
            return -1;
        }
        step += sqrt(n);
    }

    while (a[pre] < x) {
        pre++;
        if (pre == min(step, n)) {
            return -1;
        }
    }

    if (a[pre] == x) {
        return pre;
    }

    return -1;
}

// SEARCH FUNCTION for double
int jump_search_double(double a[], int n, double x) {
    int step = sqrt(n);
    int pre = 0;

    while (a[min(step, n) - 1] < x) {
        pre = step;
        if (pre >= n) {
            return -1;
        }
        step += sqrt(n);
    }

    while (a[pre] < x) {
        pre++;
        if (pre == min(step, n)) {
            return -1;
        }
    }

    if (a[pre] == x) {
        return pre;
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
    int res = jump_search_int(a, n, x);
    if (res != -1) {
        cout << x << " is at index " << res << " of the array." << endl;
    } else {
        cout << x << " is not found in the array." << endl;
    }

    // Generate a large test array
    int test_size = 10000000;
    int* test_array = new int[test_size];
    generate_large_sorted_test_array(test_array, test_size);

    // Measure time for jump search
    int search_value = test_size / 2; // Search for the middle value
    clock_t start = clock();
    int search_result = jump_search_int(test_array, test_size, search_value);
    clock_t end = clock();
    cout << "Jump Search time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Measure time for std::binary_search
    start = clock();
    bool std_search_result = binary_search(test_array, test_array + test_size, search_value);
    end = clock();
    cout << "std::binary_search time: " << double(end - start) / CLOCKS_PER_SEC << " seconds" << endl;

    // Cleanup
    delete[] test_array;

    return 0;
}

