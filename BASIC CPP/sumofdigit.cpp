#include <iostream>
using namespace std;

int main() {
    int num, sum = 0;
    
    cout << "Enter a number: ";
    cin >> num;

    while (num != 0) {
        int digit = num % 10;   // Extract last digit
        sum += digit;           // Add to sum
        num /= 10;              // Remove last digit
    }

    cout << "Sum of digits = " << sum << endl;

    return 0;
}
