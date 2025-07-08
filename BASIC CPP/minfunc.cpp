#include <iostream>
using namespace std;
int minOftwo (int a, int b)
{
    if(a<b)
    {
        return a;
    }
    else{
        return b;
    }
}
int main()
{
    cout << "min = "<< minOftwo(10,5)<< endl;
}