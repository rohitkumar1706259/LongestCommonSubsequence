#include <iostream>
using namespace std;

int main() {
	int ts;
	cin>>ts;
	for(int m=0;m<ts;m++){
	
	    int f_len,s_len;
	 	  cin>>f_len>>s_len;
			
	    string f,s;
	    
		cin.ignore();
	    getline(cin,f);
	    //cin.ignore();
		getline(cin,s);
		
		cout<<f<<endl;
		cout<<s;
		
	    f_len=f.length();
	    s_len=s.length();
	    

	    int L[f_len+1][s_len+1];
	    for(int z=0;z<=f_len;z++)
	    {
	        L[z][0]=0;
	    }
	    for(int z=0;z<=s_len+1;z++)
	    {
	        L[0][z]=0;
	    }
	    for(int j=1;j<=f_len;j++)
	    {
	        for(int k=1;k<=s_len;k++)
	        {
	            if(s[j-1]==f[k-1])
	            {
	                L[j][k]=L[j-1][k-1]+1;
	                cout<<L[j][k];
	            }
	            else
			    {
	                L[j][k]=max(L[j-1][k],L[j][k-1]);
	                cout<<L[j][k];
	            }
	        }
	    }
	   // cout<<"hi";
	    cout<<L[f_len][s_len]<<endl;
	}
	
}
