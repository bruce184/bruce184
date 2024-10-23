#include<bits/stdc++.h>
#pragma GCC optimize ("O3,unroll-loops")
#define Sanic_speed ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define Ret return 0;
#define ret return;
#define all(x) x.begin(), x.end()
#define eln "\n";
#define elif else if
#define ll long long int
#define fi first
#define se second
#define frs(i, a, b) for(int i = a; i < b; ++i)
#define fre(i, a, b) for(int i = a; i <= b; ++i)
#define wh(t) while (t--)
#define SORAI int main()
#define fileinout(name) freopen(name".INP", "r", stdin);freopen(name".OUT", "w", stdout);
using namespace std;

const int MOD = 1e9 + 7;
const int INF = 1e9 + 7;
const ll INFLL = (ll)1e18 + 7;

///Đỉnh có kiểu là chuỗi ký tự
/// Tập đỉnh: có thể dùng cấu trúc dãy hoặc dslk đơn để lưu trữ
///Tập cạnh: cấu trúc dãy lưu các cạnh
typedef int dinh;
struct tapdinh {
    int n; //số đỉnh
    dinh v[30]; //giả sử tối đa là 30 đỉnh
};

struct canh {
    dinh x, y;
    double w; //trọng số (nếu có)
};

struct tapcanh {
    int n; //số cạnh
    canh e[30*29/2]; // 3 đỉnh -> 3 cạnh, 4 đỉnh -> 6 cạnh
};

struct dothi {
    tapdinh V;
    tapcanh E;
};

void nhap (dothi& G) {
    //Nhập tập đỉnh
    cout << "So dinh: "; cin >> G.V.n;
    cout << "Nhap: " << G.V.n << "dinh: ";
    for (i, 0, G.V.n) {
        cin<< G.V.v;
    }
    //Nhập tập cạnh
    cout << "So anh: "; cin >> G.E.n;
    cout << "Nhap: " << G.E.n << "canh: ";
    for (i, 0, G.E.n) {
        cin << G.E.e[i].x << G.E.e[i].y;
    }
}

void xuat(dothi G) {
	// xuat tap dinh
	cout << "So dinh = " << G.V.n << eln;
	cout << "Tap cac dinh:" << eln;
	for (int i = 0; i < G.V.n; i++)
		cout << G.V.v[i] << "  ";
	cout << eln;
	// xuat tap canh
	cout << "So canh = "<< G.E.n << eln;
	cout << "Tap cac canh:" << eln;
	for (int i = 0; i < G.E.n; i++)
		cout << "{" << G.E.e[i].x << "," << G.E.e[i].y << "}  ";
	cout << eln
}

int deg(dinh a, dothi G) {
    int counts = 0;
    frs(i, 0, G.E.n) {
        if (G.E.e[i].x == a || G.E.e[i].y == a) {++counts;}
    }
    return counts;
}

SORAI {

}
