#include<iostream>
using namespace std;
int n=5,i,j;

void square()
{
          for(int i=0;i<=n;i++)
{
      for(int j=0;j<=n;j++){
         cout<<"*";
      }
     cout<<endl;
}
}

void lowerTriangle(){
      for (i=0;i<=n-1;i++)
{
        for(j=0;j<=i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
}
int main()
{
    square();
    lowerTriangle();
    // square();
return 0;
}