#include <iostream>
using namespace std;
int bintoDecimal(int n)
{
    int ans=0,pow=1;

    while(n>0)
    {
        int lastDigit=n%10;
        ans+=lastDigit*pow;
        pow*=2;
        n/=10;
    }
return ans;
}
int main()
{
    int n;
    cout << "Enter a binary number: ";
    cin >> n;
    int decimal = bintoDecimal(n);
    cout << "Decimal: " << decimal << endl;   
    return 0;
}