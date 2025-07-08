// C++ program to convert decimal to binary using 
#include <iostream>
#include <vector>   
using namespace std;

int decimalToBinary(int n) {
    int ans = 0, pow = 1;
    while (n > 0) {
        int lastDigit = n % 2;
        ans += lastDigit * pow;
        pow *= 10;
        n /= 2;
    }
    return ans;
}
int main()
{
    int n;
    cout << "Enter a decimal number: ";
    cin >> n;
    int binary = decimalToBinary(n);
    cout << "Binary: " << binary << endl;   
    return 0;
}