#include <stdio.h>
// #include <string.h>
#define MILLION 1000000
typedef long long LL;

LL p[MILLION];
bool sieve[MILLION]; // memset not needed cuz preset to zero

int main() {
	LL T, N, P = 0, answer, pp;
	
	// precalculate all primes under a million.
	// memset(sieve,false,sizeof(sieve));
	for (LL i = 2; i < MILLION; i++) {
		if (sieve[i])
			continue;
		
		p[P++] = i;
		
		for (LL j = i*2; j < MILLION; j += i)
			sieve[j] = true;
	}
	
	// Now read input data.
	scanf("%lld", &T);
	for (LL t = 1; t <= T; t++) {
		scanf("%lld", &N);
		
		if (N == 1) {
			// 1 is a weird case.
			// Normally it can be discounted by coming in last for best case,
			// and can be countd by coming in first for worst case.
			answer = 0;
		}
		
		else {
			// If N is not 1, you get a free extra
			answer = 1;
			for (LL i = 0; i < P; i++) {
				LL pp = p[i] * p[i];
				
				if (pp > N)
					break;
				
				for (; pp <= N; pp *= p[i])
					answer++;
			}
		}
		
		printf("Case #%lld: %lld\n", t, answer);
	}
}