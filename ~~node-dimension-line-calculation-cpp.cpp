#include <bigint.h>
using namespace std;

int factorial(int n) 
{
    // single line to find factorial
    return (n==1 || n==0) ? 1: n*factorial(n-1);
}

int main() {
    int sigma = 0;
    int totalLines = 0;
    int SideLength = 0;
    int Dimension = 0;
    int nodes = 0;

    cout << "How long do you want each side to be?\n";
    cin >> SideLength;
    cout << "How many dimensions do you do you want your shape to occupy?\n";
    cin >> Dimension;

    nodes = pow(SideLength, Dimension);

    for (int i = 1; i < nodes; i++) {
        sigma = sigma + i;
    }
    cout << "\nTotal iterations will be: " << sigma << "\n";

    for (int x = 0; x < nodes; ++x) {
        int a = factorial(sigma);
        int b = factorial(x);
        int c = pow(sigma, (sigma - x));
        cout << c << ", ";
        //int n = (a/n)*c;
        //totalLines = totalLines + n;
    }
    cout << totalLines;
}