#include<bits/stdc++.h>
using namespace std;
void ascending(vector<int>v2)
{
	int j,key;
    for (int i = 1; i < v2.size(); i++)
    {
        key = v2[i];
        j = i - 1;
 
        while (j >= 0 && v2[j] > key)
        {
            v2[j + 1] = v2[j];
            j = j - 1;
        }
        v2[j + 1] = key;
    }
    cout<<"sorted element=";
	for(int i=0;i<v2.size();i++)
	{
		cout<<v2[i]<<" ";
	}
}
int main()
{
	vector<int>v1;
	int n;
	cout<<"enter the number of element to sort=";

	cin>>n;
		cout<<n<<endl;
	for(int i=0;i<n;i++)
	{
		int x;
		cin>>x;
		v1.push_back(x);
	}
	ascending(v1);
}