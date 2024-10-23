#ifndef HEADER_H
#define HEADER_H

#include <bits/stdc++.h>

using namespace std;

template<typename T>
void doSwap(T& a, T& b) {
    T tmp = a;
    a = b;
    b = tmp;
}

template<typename T>
void bubbleSort(vector<T>& a) {
    int n = a.size();
    bool isSwapped;
    do {
        isSwapped = false;
        for (int i = 0; i < n - 1; i++) {
            if (a[i] > a[i + 1]) {
                doSwap(a[i], a[i + 1]);
                isSwapped = true;
            }
        }
        n--;
    } while (isSwapped);
}

template<typename T>
bool binarySearch(const vector<T>& a, T value, int left, int right) {
    if (left > right) {
        return false;
    }

    int mid = left + (right - left) / 2;
    if (a[mid] == value) {
        return true;
    }
    else if (a[mid] > value) {
        return binarySearch(a, value, left, mid - 1);
    }
    else {
        return binarySearch(a, value, mid + 1, right);
    }
}

#endif
