#include <iostream>
#include <cmath>
using namespace std;

int main() {
    float x, y;
    for (y = 1.5; y > -1.5; y -= 0.1) {
        for (x = -1.5; x < 1.5; x += 0.05) {
            float a = x * x + y * y ;
            if (a * a * a - x * x * y * y * y <= 0.0)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
    return 0;
}
