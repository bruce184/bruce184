/*BUBBLE SORT (gần giống Insertion Sort): Sắp xếp nổi bọt trên dãy ban đầu không có thứ tự
Time Complexity: O(n^2)
Space Complexity: O(1)
Idea:
    1. Start both loop at the 1st index
    2. (In the second loop) Compare the current value to the next one, if it is greater <-> SWAP THEM
    3. Continue until the array is sorted
*/


// INCLUDE LIBRARY
#include<bits/stdc++.h>
using namespace std;

// BUBBLE SORT FUNCTION for int
void bubble_sort_int(int a[], int n){
    bool swapped;
    for (int i = 0; i < n; i++){
        swapped = false;
        for (int j = 0; j < n - i - 1; j++){
            if (a[j] > a[j + 1]){
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }

}
}

// BUBBLE SORT FUNCTION for double
void bubble_sort_double(double a[], int n){
    bool swapped;
    for (int i = 0; i < n; i++){
        swapped = false;
        for (int j = 0; j < n - i - 1; j++){
            if (a[j] > a[j + 1]){
                swap(a[j], a[j + 1]);
                swapped = true;
            }
        }
        // Print the array after each pass
        cout << "Array after pass " << i + 1 << ": ";
        for (int k = 0; k < n; k++) {
            cout << a[k] << " ";
        }
        cout << endl;
        if (!swapped) break;
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
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }

    // Call the function to sort the original array of integers
    bubble_sort_int(a, n);

    // Print out the sorted array
    cout << "The array after being sorted: ";
    for (int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
    cout << endl;

    // Check if the array is sorted correctly
    if (is_sorted_int(a, n)) {
        cout << "Bubble Sort result is correct!" << endl;
    } else {
        cout << "Bubble Sort result is incorrect!" << endl;
    }

    // sort(a, a + n);


    return 0;
}
