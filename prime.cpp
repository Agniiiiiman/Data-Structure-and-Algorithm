#include<iostream>
using namespace std;
int main()
{
    int n;
    cout<<"ENTER A NUMBER ";// printf("ENTER A NUMBER ");
    cin >> n;//scanf("%d",&n);
  
    bool isPrime =true;
    for (int i= 2;i<=(n-1);i++)
    {
        if(n%i==0)
        {
            isPrime = false;
            break;
        }
    }
    if(isPrime==true)
    {
        cout<<"PRIME NUMBER \n";//printf("PRIME NUMBER ");

    }
    else{
        cout<<"NOT A PRIME NUMBER \n";//printf("NOT A PRIME NUMBER");
    }
    return 0;
}