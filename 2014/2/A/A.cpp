#include <iostream>
using namespace std;
#define MAX_N 10000

int T, N, X, S[MAX_N];
bool U[MAX_N];

int test(int M) {
	for (int i = 0; i < M; i++)
		U[i] = false;
	
	for (int i = M; i < N; i++) {
		for (int j = M-1; j >= 0; j--) {
			if (!U[j] && S[i]+S[j] <= X) {
				U[i] = true;
				break;
			}
		}
	}
	
	int total = N;
	for (int i = 0; i < M; i++)
		if (U[i])
			total--;
	
	return total;
}

int main() {
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> X;
		
		for (int i = 0; i < N; i++) {
			cin >> S[i];
		}
		
		int ans = 10000000;
		for (int i = 0; i <= N; i++) {
			if (ans > test(i))
				ans = test(i);
		}
		cout << "Case #" << t << ":" << ans << endl;;
	}
}