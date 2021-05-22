#include<bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define pb push_back
#define int long long
#define ldd long double
#define vec_i vector<int>
#define sz(x) (int)(x.size())
#define all(x) (x).begin(),(x).end()
#define forr(x,a,m) for(int x=a;x<m;x+=1)
const int mod = 1000000007;

void solve() {
	int n; cin >> n;
	int a[n]; forr(i, 0, n) cin >> a[i];
	forr(i,0,n) cout<<a[i]+1<<' ';
	cout<<'\n';
}

signed main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	int tin = 1; //cin>>tin;
	while (tin--) { solve(); }
	return 0;
}










